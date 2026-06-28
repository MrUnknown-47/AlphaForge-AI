import uuid
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.modules.technical.models import IndicatorsCacheModel

class TechnicalRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_latest_indicators(self, ticker: str) -> IndicatorsCacheModel | None:
        stmt = (
            select(IndicatorsCacheModel)
            .where(IndicatorsCacheModel.ticker == ticker)
            .order_by(IndicatorsCacheModel.time.desc())
        )
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def save_indicator_cache(self, model: IndicatorsCacheModel) -> IndicatorsCacheModel:
        self.db.add(model)
        await self.db.commit()
        return model