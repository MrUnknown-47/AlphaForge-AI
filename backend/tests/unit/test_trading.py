import pytest
from decimal import Decimal
from unittest.mock import MagicMock
from app.modules.trading.order_validator import OrderValidator
from app.modules.trading.models import OrderModel
from app.modules.trading.exceptions import OrderValidationError

def test_order_validation_invalid_quantity():
    validator = OrderValidator()
    order = OrderModel(quantity=0, type="MARKET", side="BUY")
    
    with pytest.raises(OrderValidationError):
        validator.validate_order(order, Decimal("180.00"))

def test_order_validation_excessive_price_deviation():
    validator = OrderValidator()
    order = OrderModel(quantity=10, type="LIMIT", price=300.00, side="BUY")
    
    with pytest.raises(OrderValidationError):
        # Current price 100.00 vs Limit price 300.00 is >50% deviation
        validator.validate_order(order, Decimal("100.00"))