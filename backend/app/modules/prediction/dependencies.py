from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.database import get_db
from app.modules.prediction.repository import PredictionRepository
from app.modules.prediction.service import PredictionService
from app.modules.prediction.facade import PredictionFacade
from app.modules.feature_store.facade import FeatureStoreFacade
from app.modules.feature_store.dependencies import get_feature_store_facade

async def get_prediction_repo(db: AsyncSession = Depends(get_db)) -> PredictionRepository:
    return PredictionRepository(db)

async def get_prediction_service(
    repo: PredictionRepository = Depends(get_prediction_repo),
    feature_facade: FeatureStoreFacade = Depends(get_feature_store_facade)
) -> PredictionService:
    return PredictionService(repo, feature_facade)

async def get_prediction_facade(
    service: PredictionService = Depends(get_prediction_service)
) -> PredictionFacade:
    return PredictionFacade(service)
