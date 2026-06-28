import uuid
from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field
from decimal import Decimal

class SentimentScoreCreate(BaseModel):
    ticker: str = Field(..., max_length=16)
    sentiment_label: str = Field(..., pattern="^(BULLISH|BEARISH|NEUTRAL)$")
    confidence_score: Decimal = Field(..., ge=0, le=1)

class SentimentScoreResponse(BaseModel):
    id: uuid.UUID
    article_id: uuid.UUID
    ticker: str
    sentiment_label: str
    confidence_score: Decimal
    created_at: datetime

    class Config:
        from_attributes = True

class NewsArticleCreate(BaseModel):
    source: str = Field(..., max_length=255)
    headline: str = Field(..., max_length=512)
    content: str | None = None
    url: str | None = Field(None, max_length=1024)
    published_at: datetime

class NewsArticleResponse(BaseModel):
    id: uuid.UUID
    source: str
    headline: str
    content: str | None
    url: str | None
    published_at: datetime

    class Config:
        from_attributes = True

class ArticleSentimentResponse(NewsArticleResponse):
    sentiment_scores: list[SentimentScoreResponse] = []