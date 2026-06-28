from app.modules.technical.service import TechnicalService
from app.modules.technical.schemas import IndicatorsCacheResponse

class TechnicalFacade:
    """
    Unified entry point for prediction engine or strategy modules to query indicator matrices.
    """
    def __init__(self, service: TechnicalService):
        self._service = service

    async def get_latest_indicators(self, ticker: str) -> IndicatorsCacheResponse | None:
        model = await self._service.fetch_cached_indicators(ticker)
        if model:
            return IndicatorsCacheResponse.from_orm(model)
        return None

    async def compute_custom_indicator(self, ticker: str, name: str, params: dict) -> list:
        return await self._service.calculate_indicator(ticker, name, params)