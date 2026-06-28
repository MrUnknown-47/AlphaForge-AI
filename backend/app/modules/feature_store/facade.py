from datetime import datetime
from app.modules.feature_store.service import FeatureStoreService

class FeatureStoreFacade:
    """
    Interface gateway for ML models or execution simulators to load calculated features.
    """
    def __init__(self, service: FeatureStoreService):
        self._service = service

    async def get_latest_online_features(self, tickers: list[str]) -> list[dict]:
        return await self._service.get_latest_online_features(tickers)

    async def trigger_historical_backfill(self, tickers: list[str], start_date: datetime, end_date: datetime) -> None:
        await self._service.run_backfill(tickers, start_date, end_date)