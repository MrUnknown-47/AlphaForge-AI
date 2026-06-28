import logging
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.feature_store.models import (
    TechnicalFeaturesModel,
    MarketFeaturesModel,
    FundamentalFeaturesModel,
    SentimentFeaturesModel
)

logger = logging.getLogger(__name__)

class FeatureStoreRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_latest_technical_features(self, ticker: str) -> TechnicalFeaturesModel | None:
        stmt = select(TechnicalFeaturesModel).where(TechnicalFeaturesModel.ticker == ticker).order_by(TechnicalFeaturesModel.time.desc())
        res = await self.db.execute(stmt)
        return res.scalars().first()

    async def get_latest_market_features(self, ticker: str) -> MarketFeaturesModel | None:
        stmt = select(MarketFeaturesModel).where(MarketFeaturesModel.ticker == ticker).order_by(MarketFeaturesModel.time.desc())
        res = await self.db.execute(stmt)
        return res.scalars().first()

    async def get_latest_fundamental_features(self, ticker: str) -> FundamentalFeaturesModel | None:
        stmt = select(FundamentalFeaturesModel).where(FundamentalFeaturesModel.ticker == ticker).order_by(FundamentalFeaturesModel.time.desc())
        res = await self.db.execute(stmt)
        return res.scalars().first()

    async def get_latest_sentiment_features(self, ticker: str) -> SentimentFeaturesModel | None:
        stmt = select(SentimentFeaturesModel).where(SentimentFeaturesModel.ticker == ticker).order_by(SentimentFeaturesModel.time.desc())
        res = await self.db.execute(stmt)
        return res.scalars().first()

    async def insert_technical_features_batch(self, rows: list[dict]) -> None:
        if not rows:
            return
        stmt = insert(TechnicalFeaturesModel)
        await self.db.execute(stmt, rows)
        await self.db.commit()

    async def insert_market_features_batch(self, rows: list[dict]) -> None:
        if not rows:
            return
        stmt = insert(MarketFeaturesModel)
        await self.db.execute(stmt, rows)
        await self.db.commit()

    async def insert_fundamental_features_batch(self, rows: list[dict]) -> None:
        if not rows:
            return
        stmt = insert(FundamentalFeaturesModel)
        await self.db.execute(stmt, rows)
        await self.db.commit()

    async def insert_sentiment_features_batch(self, rows: list[dict]) -> None:
        if not rows:
            return
        stmt = insert(SentimentFeaturesModel)
        await self.db.execute(stmt, rows)
        await self.db.commit()