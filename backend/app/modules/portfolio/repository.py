import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.modules.portfolio.models import PortfolioModel, HoldingModel, TransactionModel, PortfolioMetricsModel

class PortfolioRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_portfolio(self, portfolio_id: uuid.UUID) -> PortfolioModel | None:
        stmt = select(PortfolioModel).where(PortfolioModel.id == portfolio_id)
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def get_user_portfolios(self, user_id: uuid.UUID) -> list[PortfolioModel]:
        stmt = select(PortfolioModel).where(PortfolioModel.user_id == user_id)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def create_portfolio(self, portfolio: PortfolioModel) -> PortfolioModel:
        self.db.add(portfolio)
        await self.db.commit()
        await self.db.refresh(portfolio)
        return portfolio

    async def update_cash_balance(self, portfolio_id: uuid.UUID, amount: float) -> PortfolioModel:
        portfolio = await self.get_portfolio(portfolio_id)
        if portfolio:
            portfolio.cash_balance += amount
            await self.db.commit()
            await self.db.refresh(portfolio)
        return portfolio

    async def get_holdings(self, portfolio_id: uuid.UUID) -> list[HoldingModel]:
        stmt = select(HoldingModel).where(HoldingModel.portfolio_id == portfolio_id)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def create_transaction(self, tx: TransactionModel) -> TransactionModel:
        self.db.add(tx)
        await self.db.commit()
        return tx

    async def save_metrics(self, metrics: PortfolioMetricsModel) -> PortfolioMetricsModel:
        self.db.add(metrics)
        await self.db.commit()
        return metrics