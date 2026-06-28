from app.modules.prediction.service import PredictionService
from app.modules.prediction.schemas import PredictionResponse

class PredictionFacade:
    """
    Interface gateway for trading matching engines or risk calculators to load target forecasts.
    """
    def __init__(self, service: PredictionService):
        self._service = service

    async def get_latest_forecasts(self, ticker: str, horizon: str, limit: int = 10) -> list[PredictionResponse]:
        models = await self._service.get_predictions(ticker, horizon, limit)
        return [PredictionResponse.from_orm(m) for m in models]

    async def run_training_pipeline(self, ticker: str, horizon: str, model_type: str = "XGBoost") -> None:
        await self._service.train_and_register_pipeline(ticker, horizon, model_type)