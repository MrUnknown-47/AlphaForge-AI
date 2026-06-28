from decimal import Decimal
from app.modules.trading.models import OrderModel
from app.modules.trading.exceptions import OrderValidationError

class OrderValidator:
    def validate_order(self, order: OrderModel, current_price: Decimal) -> None:
        """
        Validates basic parameter configurations.
        """
        if order.quantity <= 0:
            raise OrderValidationError("Order quantity must be positive")

        if order.type in ("LIMIT", "STOP_LIMIT") and (order.price is None or order.price <= 0):
            raise OrderValidationError("Limit orders require a valid positive execution price limit")

        # Price verification: prevent unrealistic paper trades (e.g. limit price deviances > 50%)
        if order.type == "LIMIT" and order.price:
            limit_price = Decimal(str(order.price))
            dev = abs(limit_price - current_price) / current_price
            if dev > Decimal("0.50"):
                raise OrderValidationError("Order limit price deviancy exceeds maximum allowed thresholds (50%)")
