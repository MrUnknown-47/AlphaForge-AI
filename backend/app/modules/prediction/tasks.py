import logging
import asyncio
from celery import Celery
from app.shared.database import db_manager
from app.modules.prediction.repository import PredictionRepository
from app.modules.prediction.service import PredictionService
from app.modules.feature_store.facade import FeatureStoreFacade
from app.modules.feature_store.repository import FeatureStoreRepository
from app.modules.feature_store.feature_pipeline import FeaturePipeline

# Injects other facades
from app.modules.market_data.facade import MarketDataFacade
from app.modules.market_data.repository import MarketDataRepository
from app.modules.market_data.service import MarketDataService

from app.modules.fundamental.facade import FundamentalFacade
from app.modules.fundamental.repository import FundamentalRepository
from app.modules.fundamental.service import FundamentalService

from app.modules.sentiment.facade import SentimentFacade
from app.modules.sentiment.repository import SentimentRepository
from app.modules.sentiment.service import SentimentService

from app.modules.technical.facade import TechnicalFacade
from app.modules.technical.repository import TechnicalRepository
from app.modules.technical.service import TechnicalService

logger = logging.getLogger(__name__)

# Initialize Celery app
celery_app = Celery("prediction_tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

async def _train_all_active_models() -> None:
    async with db_manager.session() as db:
        repo = PredictionRepository(db)
        
        # Instantiate Feature Store Facade dependencies
        market_facade = MarketDataFacade(MarketDataService(MarketDataRepository(db)))
        fundamental_facade = FundamentalFacade(FundamentalService(FundamentalRepository(db)))
        sentiment_facade = SentimentFacade(SentimentService(SentimentRepository(db)))
        technical_facade = TechnicalFacade(TechnicalService(TechnicalRepository(db), market_facade))
        
        pipeline = FeaturePipeline(
            market_facade=market_facade,
            fundamental_facade=fundamental_facade,
            sentiment_facade=sentiment_facade,
            technical_facade=technical_facade
        )
        
        feature_facade = FeatureStoreFacade(FeatureStoreRepository(db), pipeline)
        service = PredictionService(repo, feature_facade)
        
        tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "AMD", "SPY", "QQQ"]
        horizons = ["1d", "5d"]
        
        logger.info("Executing scheduled weekly ML model retraining job...")
        for ticker in tickers:
            for horizon in horizons:
                try:
                    # Retrain active XGBoost estimators weekly
                    await service.train_and_register_pipeline(ticker, horizon, model_type="XGBoost")
                except Exception as e:
                    logger.error(f"Weekly training failed for {ticker} ({horizon}): {e}")

@celery_app.task(name="prediction.train_weekly")
def train_models_weekly() -> None:
    """
    Celery scheduled task runner.
    Executes model updates in background threads weekly.
    """
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    loop.run_until_complete(_train_all_active_models())