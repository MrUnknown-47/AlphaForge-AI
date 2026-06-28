from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.database import get_db
from app.modules.feature_store.repository import FeatureStoreRepository
from app.modules.feature_store.feature_pipeline import FeaturePipeline
from app.modules.feature_store.service import FeatureStoreService
from app.modules.feature_store.facade import FeatureStoreFacade

# Facades dependencies
from app.modules.market_data.facade import MarketDataFacade
from app.modules.market_data.dependencies import get_market_facade
from app.modules.fundamental.facade import FundamentalFacade
from app.modules.fundamental.dependencies import get_fundamental_facade
from app.modules.sentiment.facade import SentimentFacade
from app.modules.sentiment.dependencies import get_sentiment_facade
from app.modules.technical.facade import TechnicalFacade
from app.modules.technical.dependencies import get_technical_facade

async def get_feature_store_repo(db: AsyncSession = Depends(get_db)) -> FeatureStoreRepository:
    return FeatureStoreRepository(db)

async def get_feature_store_service(
    repo: FeatureStoreRepository = Depends(get_feature_store_repo),
    market_facade: MarketDataFacade = Depends(get_market_facade),
    fundamental_facade: FundamentalFacade = Depends(get_fundamental_facade),
    sentiment_facade: SentimentFacade = Depends(get_sentiment_facade),
    technical_facade: TechnicalFacade = Depends(get_technical_facade)
) -> FeatureStoreService:
    pipeline = FeaturePipeline(
        market_facade=market_facade,
        fundamental_facade=fundamental_facade,
        sentiment_facade=sentiment_facade,
        technical_facade=technical_facade
    )
    return FeatureStoreService(repo, pipeline)

async def get_feature_store_facade(
    service: FeatureStoreService = Depends(get_feature_store_service)
) -> FeatureStoreFacade:
    return FeatureStoreFacade(service)
