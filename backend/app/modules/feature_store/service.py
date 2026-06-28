import logging
from datetime import datetime
from app.modules.feature_store.repository import FeatureStoreRepository
from app.modules.feature_store.feature_pipeline import FeaturePipeline
from app.modules.feature_store.schemas import FeatureQuery, FeatureSetResponse
from app.shared.cache import cache_manager

logger = logging.getLogger(__name__)

class FeatureStoreService:
    def __init__(self, repo: FeatureStoreRepository, pipeline: FeaturePipeline) -> None:
        self.repo = repo
        self.pipeline = pipeline

    async def generate_features_for_ticker(self, ticker: str, start_date: datetime, end_date: datetime) -> None:
        logger.info(f"Executing feature computation pipeline for {ticker} from {start_date.date()} to {end_date.date()}")
        
        feature_dfs = await self.pipeline.compute_feature_set(ticker, start_date, end_date)
        if not feature_dfs:
            logger.warning(f"Feature computation pipeline returned empty results for {ticker}.")
            return

        # 1. Extract and Batch Insert to Database tables
        df_market = feature_dfs.get("market")
        if df_market is not None and not df_market.empty:
            market_rows = df_market.to_dict(orient="records")
            await self.repo.insert_market_features_batch(market_rows)

        df_tech = feature_dfs.get("technical")
        if df_tech is not None and not df_tech.empty:
            tech_rows = df_tech.to_dict(orient="records")
            await self.repo.insert_technical_features_batch(tech_rows)

        df_fund = feature_dfs.get("fundamental")
        if df_fund is not None and not df_fund.empty:
            fund_rows = df_fund.to_dict(orient="records")
            await self.repo.insert_fundamental_features_batch(fund_rows)

        df_sentiment = feature_dfs.get("sentiment")
        if df_sentiment is not None and not df_sentiment.empty:
            sentiment_rows = df_sentiment.to_dict(orient="records")
            await self.repo.insert_sentiment_features_batch(sentiment_rows)

        # 2. Update Low-Latency Online Cache (Redis) with latest calculations
        cache_key = f"feature:latest:{ticker}"
        
        latest_features = {
            "timestamp": end_date.isoformat(),
            "ticker": ticker
        }
        
        if df_market is not None and not df_market.empty:
            latest_features.update({
                "returns_1d": float(df_market["returns_1d"].iloc[-1]),
                "returns_5d": float(df_market["returns_5d"].iloc[-1]),
                "returns_20d": float(df_market["returns_20d"].iloc[-1]),
                "realized_vol_20": float(df_market["realized_vol_20"].iloc[-1]),
                "market_beta": float(df_market["market_beta"].iloc[-1]),
                "spy_correlation": float(df_market["spy_correlation"].iloc[-1]),
                "qqq_correlation": float(df_market["qqq_correlation"].iloc[-1])
            })
            
        if df_tech is not None and not df_tech.empty:
            latest_features.update({
                "rsi": float(df_tech["rsi"].iloc[-1]),
                "macd": float(df_tech["macd"].iloc[-1]),
                "atr": float(df_tech["atr"].iloc[-1]),
                "bollinger_width": float(df_tech["bollinger_width"].iloc[-1]),
                "ema_10": float(df_tech["ema_10"].iloc[-1]),
                "ema_200": float(df_tech["ema_200"].iloc[-1])
            })
            
        if df_fund is not None and not df_fund.empty:
            latest_features.update({
                "pe_ratio": float(df_fund["pe_ratio"].iloc[-1]),
                "pb_ratio": float(df_fund["pb_ratio"].iloc[-1]),
                "roe": float(df_fund["roe"].iloc[-1]),
                "debt_to_equity": float(df_fund["debt_to_equity"].iloc[-1])
            })

        if df_sentiment is not None and not df_sentiment.empty:
            latest_features.update({
                "sentiment_mean": float(df_sentiment["sentiment_mean"].iloc[-1]),
                "sentiment_change": float(df_sentiment["sentiment_change"].iloc[-1])
            })

        await cache_manager.set_json(cache_key, latest_features, ttl=86400) # Cache for 24h
        logger.info(f"Feature computation pipeline successfully committed for {ticker}.")

    async def get_latest_online_features(self, tickers: list[str]) -> list[dict]:
        results = []
        for ticker in tickers:
            cache_key = f"feature:latest:{ticker}"
            cached = await cache_manager.get_json(cache_key)
            if cached:
                results.append(cached)
            else:
                # Fallback to database queries
                pass
        return results

    async def run_backfill(self, tickers: list[str], start_date: datetime, end_date: datetime) -> None:
        """Runs batch historical backfilling for multiple symbols."""
        for ticker in tickers:
            try:
                await self.generate_features_for_ticker(ticker, start_date, end_date)
            except Exception as e:
                logger.error(f"Failed historical feature backfilling for {ticker}: {e}")