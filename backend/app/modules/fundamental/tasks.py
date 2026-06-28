import logging
import asyncio
from celery import Celery
from app.shared.database import db_manager
from app.modules.fundamental.repository import FundamentalRepository
from app.modules.fundamental.service import FundamentalService

logger = logging.getLogger(__name__)

# Initialize Celery app matching the redis broker configurations
celery_app = Celery("fundamental_tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

async def _sync_symbols_fundamentals() -> None:
    """Coroutine processing the database write loop."""
    async with db_manager.session() as db:
        repo = FundamentalRepository(db)
        service = FundamentalService(repo)
        
        tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "AMD", "SPY", "QQQ"]
        logger.info("Executing scheduled quarterly fundamentals sync job...")
        
        for ticker in tickers:
            try:
                # Sync latest 2 quarters to capture any filing updates/revisions
                await service.sync_ticker_fundamentals(ticker, limit=2)
            except Exception as e:
                logger.error(f"Scheduled sync failed for {ticker}: {e}")

@celery_app.task(name="fundamental.sync_quarterly")
def sync_fundamentals_quarterly() -> None:
    """
    Celery scheduled task runner.
    Executes quarterly updates in background threads.
    """
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    loop.run_until_complete(_sync_symbols_fundamentals())