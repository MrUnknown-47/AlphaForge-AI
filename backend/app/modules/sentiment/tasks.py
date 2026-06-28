import logging
import asyncio
from celery import Celery
from app.shared.database import db_manager
from app.modules.sentiment.repository import SentimentRepository
from app.modules.sentiment.service import SentimentService
from app.modules.sentiment.sentiment_engine import sentiment_engine

logger = logging.getLogger(__name__)

# Initialize Celery app mapping to Redis configurations
celery_app = Celery("sentiment_tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

async def _sync_symbols_sentiment() -> None:
    """Coroutine mapping to database scraping and inference pipelines."""
    # Ensure FinBERT is initialized on worker process memory
    sentiment_engine.initialize()
    
    async with db_manager.session() as db:
        repo = SentimentRepository(db)
        service = SentimentService(repo)
        
        tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "AMD", "SPY", "QQQ"]
        logger.info("Executing scheduled hourly news sentiment analysis job...")
        
        for ticker in tickers:
            try:
                # Scrape and score top 3 news entries from RSS feeds
                await service.scrape_and_analyze_ticker(ticker, limit=3)
            except Exception as e:
                logger.error(f"Scheduled sentiment sync failed for {ticker}: {e}")

@celery_app.task(name="sentiment.scrape_hourly")
def scrape_and_analyze_news_hourly() -> None:
    """
    Celery scheduled task runner.
    Executes RSS scraping and FinBERT inference in background worker threads.
    """
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    loop.run_until_complete(_sync_symbols_sentiment())