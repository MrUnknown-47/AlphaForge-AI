import logging
import asyncio
from datetime import datetime, timedelta
from celery import Celery
from app.shared.database import db_manager
from app.modules.feature_store.repository import FeatureStoreRepository
from app.modules.feature_store.feature_pipeline import FeaturePipeline
from app.modules.feature_store.service import FeatureStoreService

# Import facades to inject
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
celery_app = Celery("feature_store_tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

async def _recalculate_features() -> None:
    async with db_manager.session() as db:
        repo = FeatureStoreRepository(db)
        
        # Instantiate cross-module facades
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
        
        service = FeatureStoreService(repo, pipeline)
        
        tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "AMD", "SPY", "QQQ"]
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=1)
        
        logger.info("Executing scheduled daily feature engineering pipeline...")
        for ticker in tickers:
            try:
                await service.generate_features_for_ticker(ticker, start_date, end_date)
            except Exception as e:
                logger.error(f"Scheduled feature engineering failed for {ticker}: {e}")

@celery_app.task(name="feature_store.generate_daily")
def generate_features_daily() -> None:
    """
    Celery scheduled task runner.
    Triggers concurrent features calculation daily.
    """
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    loop.run_until_complete(_recalculate_features())