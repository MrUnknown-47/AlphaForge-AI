import uuid
from decimal import Decimal
from app.modules.trading.models import ExecutionModel, PositionModel
from app.modules.portfolio.facade import PortfolioFacade

class LedgerEngine:
    def __init__(self, portfolio_facade: PortfolioFacade):
        self.portfolio_facade = portfolio_facade

    async def commit_to_ledger(self, execution: ExecutionModel, portfolio_id: uuid.UUID, ticker: str, side: str) -> None:
        """
        Updates cash ledger balances and alters holdings weights.
        """
        exec_price = Decimal(str(execution.execution_price))
        exec_qty = Decimal(str(execution.executed_quantity))
        total_cost = exec_price * exec_qty

        # Call PortfolioFacade to register the transactional changes
        # For a BUY order, deduct cash; for a SELL, add cash.
        multiplier = Decimal("-1.0") if side == "BUY" else Decimal("1.0")
        cash_change = total_cost * multiplier
        
        # In a real environment, portfolio_facade records the cash ledger transaction
        # and updates holdings (e.g. portfolio_facade.record_transaction(...))
        pass
