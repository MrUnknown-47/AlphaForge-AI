import os
import logging
import asyncio
from datetime import datetime
import pandas as pd
import numpy as np
from sqlalchemy import text
from app.shared.database import db_manager

logger = logging.getLogger(__name__)

class DatasetBuilder:
    def __init__(self) -> None:
        self.universe = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "AMD", "SPY", "QQQ"]

    async def fetch_combined_features(self, ticker: str) -> pd.DataFrame:
        """
        Queries only the 19 core features from the database for the given ticker
        and merges them on time and ticker.
        """
        try:
            async with db_manager.session() as session:
                sql = f"""
                    SELECT 
                        m.time, m.ticker,
                        m.returns_1d, m.returns_5d, m.returns_20d, m.realized_vol_20, m.market_beta, m.spy_correlation, m.qqq_correlation,
                        t.rsi, t.macd, t.atr, t.bollinger_width, t.ema_10, t.ema_200,
                        f.pe_ratio, f.pb_ratio, f.roe, f.debt_to_equity,
                        s.sentiment_mean, s.sentiment_change
                    FROM feature_store.market_features m
                    LEFT JOIN feature_store.technical_features t ON m.time = t.time AND m.ticker = t.ticker
                    LEFT JOIN feature_store.fundamental_features f ON m.time = f.time AND m.ticker = f.ticker
                    LEFT JOIN feature_store.sentiment_features s ON m.time = s.time AND m.ticker = s.ticker
                    WHERE m.ticker = '{ticker}'
                    ORDER BY m.time ASC
                """
                res = await session.execute(text(sql))
                rows = res.fetchall()
                if not rows:
                    logger.warning(f"No features found in DB for {ticker}. Generating simulated dataset.")
                    return self._generate_simulated_features(ticker)
                
                cols = res.keys()
                df = pd.DataFrame(rows, columns=cols)
                return df
        except Exception as e:
            logger.error(f"Failed to fetch features from database: {e}. Falling back to simulation.")
            return self._generate_simulated_features(ticker)

    def calculate_forward_targets(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates forward return targets shifted negatively to prevent lookahead bias.
        """
        df = df.sort_values("time").reset_index(drop=True)
        df["target_1d"] = df["returns_1d"].shift(-1)
        df["target_5d"] = df["returns_5d"].shift(-5)
        df["target_20d"] = df["returns_20d"].shift(-20)

        df_clean = df.dropna(subset=["target_1d", "target_5d", "target_20d"]).reset_index(drop=True)
        return df_clean

    def temporal_split(self, df: pd.DataFrame, train_ratio: float = 0.70, val_ratio: float = 0.15) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        n = len(df)
        train_end = int(n * train_ratio)
        val_end = int(n * (train_ratio + val_ratio))

        df_train = df.iloc[:train_end].copy()
        df_val = df.iloc[train_end:val_end].copy()
        df_test = df.iloc[val_end:].copy()

        return df_train, df_val, df_test

    def save_dataset(self, df: pd.DataFrame, file_prefix: str, output_dir: str = "data/") -> None:
        os.makedirs(output_dir, exist_ok=True)
        parquet_path = os.path.join(output_dir, f"{file_prefix}.parquet")
        csv_path = os.path.join(output_dir, f"{file_prefix}.csv")

        try:
            df.to_parquet(parquet_path, index=False)
            logger.info(f"Saved Parquet dataset: {parquet_path}")
        except ImportError:
            logger.warning("pyarrow/fastparquet not installed. Falling back to CSV storage.")
            df.to_csv(csv_path, index=False)
            logger.info(f"Saved CSV dataset: {csv_path}")

    async def build_complete_dataset(self, output_dir: str = "data/") -> None:
        logger.info("Initializing Feature Dataset Builder...")
        
        all_train = []
        all_val = []
        all_test = []

        for ticker in self.universe:
            logger.info(f"Processing dataset generation for asset: {ticker}...")
            df_features = await self.fetch_combined_features(ticker)
            df_aligned = self.calculate_forward_targets(df_features)

            if len(df_aligned) < 30:
                logger.warning(f"Asset {ticker} has insufficient data rows ({len(df_aligned)}). Skipping.")
                continue

            train, val, test = self.temporal_split(df_aligned)
            all_train.append(train)
            all_val.append(val)
            all_test.append(test)

        if not all_train:
            logger.error("No valid dataset partitions generated.")
            return

        df_train_all = pd.concat(all_train, ignore_index=True)
        df_val_all = pd.concat(all_val, ignore_index=True)
        df_test_all = pd.concat(all_test, ignore_index=True)

        logger.info(f"Complete dataset compiled. Train size: {len(df_train_all)}, Val: {len(df_val_all)}, Test: {len(df_test_all)}")

        self.save_dataset(df_train_all, "train", output_dir)
        self.save_dataset(df_val_all, "validation", output_dir)
        self.save_dataset(df_test_all, "test", output_dir)

    def _generate_simulated_features(self, ticker: str) -> pd.DataFrame:
        now = datetime.utcnow()
        dates = [now - timedelta(days=i) for i in range(120)]
        dates.reverse()

        np.random.seed(42)
        df = pd.DataFrame({
            "time": dates,
            "ticker": [ticker] * 120,
            "returns_1d": np.random.normal(0.0002, 0.012, 120),
            "returns_5d": np.random.normal(0.001, 0.026, 120),
            "returns_20d": np.random.normal(0.003, 0.06, 120),
            "realized_vol_20": np.random.uniform(0.01, 0.03, 120),
            "market_beta": np.random.uniform(0.8, 1.2, 120),
            "spy_correlation": np.random.uniform(0.7, 0.9, 120),
            "qqq_correlation": np.random.uniform(0.65, 0.85, 120),
            "rsi": np.random.uniform(30, 70, 120),
            "macd": np.random.normal(0.0, 1.5, 120),
            "atr": np.random.uniform(1.0, 3.0, 120),
            "bollinger_width": np.random.uniform(0.05, 0.15, 120),
            "ema_10": np.random.uniform(100.0, 150.0, 120),
            "ema_200": np.random.uniform(90.0, 140.0, 120),
            "pe_ratio": np.random.uniform(15, 25, 120),
            "pb_ratio": np.random.uniform(2.5, 4.0, 120),
            "roe": np.random.uniform(0.10, 0.20, 120),
            "debt_to_equity": np.random.uniform(0.3, 0.7, 120),
            "sentiment_mean": np.random.uniform(-0.5, 0.5, 120),
            "sentiment_change": np.random.normal(0.0, 0.1, 120)
        })
        return df

from datetime import timedelta
