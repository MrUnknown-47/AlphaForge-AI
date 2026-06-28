from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.database import get_db
from app.modules.sentiment.repository import SentimentRepository
from app.modules.sentiment.service import SentimentService
from app.modules.sentiment.facade import SentimentFacade

async def get_sentiment_repo(db: AsyncSession = Depends(get_db)) -> SentimentRepository:
    return SentimentRepository(db)

async def get_sentiment_service(
    repo: SentimentRepository = Depends(get_sentiment_repo)
) -> SentimentService:
    return SentimentService(repo)

async def get_sentiment_facade(
    service: SentimentService = Depends(get_sentiment_service)
) -> SentimentFacade:
    return SentimentFacade(service)
