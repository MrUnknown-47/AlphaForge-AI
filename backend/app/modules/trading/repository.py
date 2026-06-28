import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.modules.trading.models import OrderModel, ExecutionModel, PositionModel, OrderEventModel

class TradingRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_order(self, order_id: uuid.UUID) -> OrderModel | None:
        stmt = select(OrderModel).where(OrderModel.id == order_id)
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def save_order(self, order: OrderModel) -> OrderModel:
        self.db.add(order)
        await self.db.commit()
        await self.db.refresh(order)
        return order

    async def save_execution(self, execution: ExecutionModel) -> ExecutionModel:
        self.db.add(execution)
        await self.db.commit()
        return execution

    async def get_position(self, portfolio_id: uuid.UUID, ticker: str) -> PositionModel | None:
        stmt = select(PositionModel).where(
            PositionModel.portfolio_id == portfolio_id,
            PositionModel.ticker == ticker
        )
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def save_position(self, position: PositionModel) -> PositionModel:
        self.db.add(position)
        await self.db.commit()
        return position

    async def save_order_event(self, event: OrderEventModel) -> OrderEventModel:
        self.db.add(event)
        await self.db.commit()
        return event