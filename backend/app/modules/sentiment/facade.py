from app.modules.sentiment.service import SentimentService
from app.modules.sentiment.schemas import ArticleSentimentResponse

class SentimentFacade:
    """
    Interface gateway for feature store or simulator modules to fetch news sentiment scores.
    """
    def __init__(self, service: SentimentService):
        self._service = service

    async def get_ticker_news_sentiment(self, ticker: str, limit: int = 10) -> list[ArticleSentimentResponse]:
        models = await self._service.get_latest_sentiment_for_ticker(ticker, limit)
        
        # Map models to Pydantic schemas (from_attributes / from_orm)
        # Note: SQLAlchemy collections map naturally
        return [ArticleSentimentResponse.from_orm(m) for m in models]