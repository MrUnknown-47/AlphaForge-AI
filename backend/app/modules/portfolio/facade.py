import uuid
from decimal import Decimal
from app.modules.portfolio.service import PortfolioService
from app.modules.portfolio.schemas import PortfolioResponse, PortfolioValuationResponse, PortfolioMetricsResponse

class PortfolioFacade:
    """
    Interface gateway for trading or risk modules to fetch assets, weights, and valuations.
    """
    def __init__(self, service: PortfolioService):
        self._service = service

    async def get_portfolio_valuation(self, portfolio_id: uuid.UUID) -> PortfolioValuationResponse:
        nav = await self._service.calculate_nav(portfolio_id)
        return PortfolioValuationResponse(
            portfolio_id=portfolio_id,
            nav=nav,
            unrealized_pnl=Decimal("0.0"), # Stubs
            realized_pnl=Decimal("0.0"),
            timestamp=datetime.utcnow() # Note: datetime must be imported
        )

    async def get_portfolio_cash(self, portfolio_id: uuid.UUID) -> Decimal:
        portfolio = await self._service.repo.get_portfolio(portfolio_id)
        if not portfolio:
            return Decimal("0.0")
        return Decimal(str(portfolio.cash_balance))

    async def verify_cash_availability(self, portfolio_id: uuid.UUID, required_amount: Decimal) -> bool:
        cash = await self.get_portfolio_cash(portfolio_id)
        return cash >= required_amount

# Import datetime inside facade to prevent build exceptions
from datetime import datetime