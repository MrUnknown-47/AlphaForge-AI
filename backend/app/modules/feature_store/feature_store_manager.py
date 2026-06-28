import pandas as pd
from app.modules.feature_store.feature_pipeline import FeaturePipeline
from app.modules.feature_store.schemas import FeatureQuery

class FeatureStoreManager:
    def __init__(self, pipeline: FeaturePipeline):
        self.pipeline = pipeline

    async def get_historical_features(self, query: FeatureQuery) -> pd.DataFrame:
        """
        Retrieves training features for target tickers across time intervals.
        """
        # Queries historical tables using repository
        return pd.DataFrame()

    async def get_online_features(self, tickers: list[str], features: list[str]) -> dict[str, dict[str, float]]:
        """
        Fetches the latest online cached features from Redis for low-latency inference.
        """
        # Read from Redis (cache_manager)
        return {}
