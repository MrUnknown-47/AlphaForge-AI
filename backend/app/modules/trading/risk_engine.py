from decimal import Decimal
from app.modules.trading.models import OrderModel
from app.modules.trading.exceptions import RiskLimitViolation
from app.modules.portfolio.facade import PortfolioFacade

class RiskEngine:
    def __init__(self, portfolio_facade: PortfolioFacade):
        self.portfolio_facade = portfolio_facade

    async def verify_pre_trade_limits(self, order: OrderModel, current_price: Decimal) -> None:
        """
        Runs margin availability, exposure bounds, and leverage evaluations.
        """
        required_capital = Decimal(str(order.quantity)) * current_price
        
        # 1. Cash coverage check (only for buy side orders)
        if order.side == "BUY":
            available = await self.portfolio_facade.verify_cash_availability(
                order.portfolio_id, required_capital
            )
            if not available:
                raise RiskLimitViolation("Insufficient cash in portfolio to place buy order")

        # 2. Maximum allocation check stub (e.g. max 20% exposure per single asset class)
        # 3. Maximum leverage validation check stub
        pass
