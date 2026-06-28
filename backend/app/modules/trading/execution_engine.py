import uuid
from decimal import Decimal
from app.modules.trading.models import OrderModel
from app.modules.trading.matching_engine import MatchingEngine
from app.modules.trading.ledger import LedgerEngine
from app.shared.cache import cache_manager

class ExecutionEngine:
    def __init__(self, matching_engine: MatchingEngine, ledger_engine: LedgerEngine):
        self.matching_engine = matching_engine
        self.ledger_engine = ledger_engine

    async def execute_trade(self, order: OrderModel, current_price: Decimal) -> None:
        """
        Runs the order against the matching engine, commits execution ledgers,
        and broadcasts transaction reports.
        """
        executions = self.matching_engine.match_order(order, current_price)
        
        for execution in executions:
            await self.ledger_engine.commit_to_ledger(
                execution,
                order.portfolio_id,
                order.ticker,
                order.side
            )
            # In a real environment, persist executions using the repository layer

        # Broadcast update over Redis Pub/Sub for WebSockets clients
        if order.status == "FILLED":
            payload = {
                "order_id": str(order.id),
                "portfolio_id": str(order.portfolio_id),
                "ticker": order.ticker,
                "status": order.status,
                "price": float(current_price)
            }
            await cache_manager.publish("trading:orders", str(payload))
