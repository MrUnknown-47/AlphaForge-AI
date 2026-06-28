import uuid
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.sentiment.models import NewsArticleModel, SentimentScoreModel

class SentimentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_article_by_url(self, url: str) -> NewsArticleModel | None:
        stmt = select(NewsArticleModel).where(NewsArticleModel.url == url)
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def save_article(self, article: NewsArticleModel) -> NewsArticleModel:
        self.db.add(article)
        await self.db.commit()
        await self.db.refresh(article)
        return article

    async def get_news_with_scores(self, ticker: str, limit: int = 20) -> list[NewsArticleModel]:
        # Perform join between articles and sentiment scores for the ticker
        stmt = (
            select(NewsArticleModel)
            .join(SentimentScoreModel)
            .where(SentimentScoreModel.ticker == ticker)
            .order_by(NewsArticleModel.published_at.desc())
            .limit(limit)
        )
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def insert_sentiment_scores_batch(self, scores: list[dict]) -> None:
        if not scores:
            return

        values = [
            {
                "article_id": s["article_id"],
                "ticker": s["ticker"],
                "sentiment_label": s["sentiment_label"],
                "confidence_score": float(s["confidence_score"])
            }
            for s in scores
        ]
        
        stmt = insert(SentimentScoreModel)
        await self.db.execute(stmt, values)
        await self.db.commit()