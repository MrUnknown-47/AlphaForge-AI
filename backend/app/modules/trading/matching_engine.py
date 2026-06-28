from decimal import Decimal
from datetime import datetime
from app.modules.trading.models import OrderModel, ExecutionModel

class MatchingEngine:
    def match_order(self, order: OrderModel, current_price: Decimal) -> list[ExecutionModel]:
        """
        Processes order against incoming bids/asks. For paper trading,
        we assume immediate execution if pricing matches constraints.
        """
        executions = []
        qty = Decimal(str(order.quantity))

        if order.type == "MARKET":
            # Market orders execute immediately at the current price
            exec_model = ExecutionModel(
                order_id=order.id,
                execution_price=float(current_price),
                executed_quantity=float(qty),
                executed_at=datetime.utcnow()
            )
            executions.append(exec_model)
            order.status = "FILLED"

        elif order.type == "LIMIT":
            limit_price = Decimal(str(order.price))
            # Buy limit filled if current price <= limit price
            # Sell limit filled if current price >= limit price
            should_execute = (
                (order.side == "BUY" and current_price <= limit_price) or
                (order.side == "SELL" and current_price >= limit_price)
            )
            if should_execute:
                exec_model = ExecutionModel(
                    order_id=order.id,
                    execution_price=float(limit_price),
                    executed_quantity=float(qty),
                    executed_at=datetime.utcnow()
                )
                executions.append(exec_model)
                order.status = "FILLED"
            else:
                order.status = "PENDING"

        return executions
