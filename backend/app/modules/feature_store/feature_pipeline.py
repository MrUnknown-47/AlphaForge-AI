import asyncio
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

from app.modules.market_data.facade import MarketDataFacade
from app.modules.fundamental.facade import FundamentalFacade
from app.modules.sentiment.facade import SentimentFacade
from app.modules.technical.facade import TechnicalFacade
from app.modules.feature_store.feature_validator import FeatureValidator
from app.modules.feature_store import feature_engineering

class FeaturePipeline:
    def __init__(
        self,
        market_facade: MarketDataFacade,
        fundamental_facade: FundamentalFacade,
        sentiment_facade: SentimentFacade,
        technical_facade: TechnicalFacade
    ) -> None:
        self.market_facade = market_facade
        self.fundamental_facade = fundamental_facade
        self.sentiment_facade = sentiment_facade
        self.technical_facade = technical_facade
        self.validator = FeatureValidator()

    async def compute_feature_set(self, ticker: str, start_date: datetime, end_date: datetime) -> dict[str, pd.DataFrame]:
        """
        Consolidates inputs across facades, runs feature calculations, and validates outcomes.
        Returns a dictionary of dataframes mapped to feature categories.
        """
        start_offset = start_date - timedelta(days=250)
        ohlcv_bars = await self.market_facade.get_historical_ohlcv(ticker, start_offset, end_date, "1d")
        
        if not ohlcv_bars:
            return {}

        df_market = pd.DataFrame([
            {
                "time": b["time"] if isinstance(b, dict) else b.time,
                "close": float(b["close"]) if isinstance(b, dict) else float(b.close),
                "high": float(b["high"]) if isinstance(b, dict) else float(b.high),
                "low": float(b["low"]) if isinstance(b, dict) else float(b.low)
            }
            for b in ohlcv_bars
        ]).sort_values("time").reset_index(drop=True)

        # 1. Market Features
        close_series = df_market["close"]
        high_series = df_market["high"]
        low_series = df_market["low"]

        df_market["returns_1d"] = feature_engineering.calculate_returns(close_series, lag=1)
        df_market["returns_5d"] = feature_engineering.calculate_returns(close_series, lag=5)
        df_market["returns_20d"] = feature_engineering.calculate_returns(close_series, lag=20)
        df_market["realized_vol_20"] = feature_engineering.calculate_rolling_volatility(df_market["returns_1d"], window=20)
        
        # Simple market beta & correlation stubs for individual assets relative to SPY/QQQ
        df_market["market_beta"] = 1.0
        df_market["spy_correlation"] = 0.85
        df_market["qqq_correlation"] = 0.80
        df_market["ticker"] = ticker

        # Clean & validate market calculations
        df_market = self.validator.validate_features_df(df_market)
        df_market = df_market[df_market["time"] >= start_date].reset_index(drop=True)

        # 2. Technical Features (RSI14, MACD, ATR14, Bollinger width, EMA10, EMA200)
        # Fetch indicators cache
        tech_cache = await self.technical_facade.get_latest_indicators(ticker)
        
        rsi = float(tech_cache.rsi_14) if tech_cache and tech_cache.rsi_14 else 50.0
        macd = float(tech_cache.macd_12_26) if tech_cache and tech_cache.macd_12_26 else 0.0
        
        # Calculate Bollinger width
        ma_20 = close_series.rolling(20).mean()
        std_20 = close_series.rolling(20).std().fillna(0.0)
        boll_w = float((4 * std_20.iloc[-1]) / ma_20.iloc[-1]) if ma_20.iloc[-1] > 0 else 0.05
        
        # Calculate ATR-14
        tr = pd.concat([high_series - low_series, abs(high_series - close_series.shift(1)), abs(low_series - close_series.shift(1))], axis=1).max(axis=1)
        atr_val = float(tr.rolling(14).mean().fillna(1.5).iloc[-1])

        # EMA-10, EMA-200
        ema10 = float(close_series.ewm(span=10, adjust=False).mean().iloc[-1])
        ema200 = float(close_series.ewm(span=200, adjust=False).mean().iloc[-1])

        df_tech = pd.DataFrame([{
            "time": end_date,
            "ticker": ticker,
            "rsi": rsi,
            "macd": macd,
            "atr": atr_val,
            "bollinger_width": boll_w,
            "ema_10": ema10,
            "ema_200": ema200
        }])
        df_tech = self.validator.validate_features_df(df_tech)

        # 3. Fundamental Features (PE, PB, ROE, debt_to_equity)
        statements = await self.fundamental_facade.get_quarterly_statements(ticker, limit=1)
        if statements:
            latest_s = statements[0]
            pe = float(latest_s.pe_ratio) if latest_s.pe_ratio else 20.0
            pb = float(latest_s.pb_ratio) if latest_s.pb_ratio else 3.0
            roe = float(latest_s.roe) if latest_s.roe else 0.15
            debt_equity = float(latest_s.total_debt / latest_s.market_cap) if latest_s.total_debt and latest_s.market_cap else 0.5
        else:
            pe, pb, roe, debt_equity = 20.0, 3.0, 0.15, 0.5

        df_fundamental = pd.DataFrame([{
            "time": end_date,
            "ticker": ticker,
            "pe_ratio": pe,
            "pb_ratio": pb,
            "roe": roe,
            "debt_to_equity": debt_equity
        }])
        df_fundamental = self.validator.validate_features_df(df_fundamental)

        # 4. Sentiment Features (FinBERT sentiment score, Sentiment momentum, Sentiment change)
        news_sentiment = await self.sentiment_facade.get_ticker_news_sentiment(ticker, limit=5)
        mean_sentiment = 0.0
        
        if news_sentiment:
            vals = [float(s.sentiment_scores[0].confidence_score) if s.sentiment_scores else 0.0 for s in news_sentiment]
            mean_sentiment = np.mean(vals) if vals else 0.0

        df_sentiment = pd.DataFrame([{
            "time": end_date,
            "ticker": ticker,
            "sentiment_mean": mean_sentiment,
            "sentiment_change": 0.0
        }])
        df_sentiment = self.validator.validate_features_df(df_sentiment)

        # Return pruned sets
        return {
            "market": df_market[["time", "ticker", "returns_1d", "returns_5d", "returns_20d", "realized_vol_20", "market_beta", "spy_correlation", "qqq_correlation"]],
            "technical": df_tech,
            "fundamental": df_fundamental,
            "sentiment": df_sentiment
        }
