from fastapi import APIRouter, Depends, Query, status
from app.modules.sentiment.facade import SentimentFacade
from app.modules.sentiment.service import SentimentService
from app.modules.sentiment.dependencies import get_sentiment_facade, get_sentiment_service
from app.modules.sentiment.schemas import ArticleSentimentResponse

router = APIRouter(prefix="/sentiment", tags=["News Sentiment Features"])

@router.get("/ticker/{ticker}", response_model=list[ArticleSentimentResponse])
async def get_ticker_news_sentiment(
    ticker: str,
    limit: int = Query(10, description="Max news articles to fetch"),
    facade: SentimentFacade = Depends(get_sentiment_facade)
):
    return await facade.get_ticker_news_sentiment(ticker, limit)

@router.post("/sync/{ticker}", status_code=status.HTTP_202_ACCEPTED)
async def sync_ticker_sentiment(
    ticker: str,
    service: SentimentService = Depends(get_sentiment_service)
):
    await service.scrape_and_analyze_ticker(ticker, limit=5)
    return {"message": f"Sentiment analysis pipeline triggered for {ticker}"}