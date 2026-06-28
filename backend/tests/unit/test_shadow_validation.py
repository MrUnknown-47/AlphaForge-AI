import pytest
from app.modules.shadow_trading.shadow_validator import ShadowValidator

def test_shadow_validation_halts():
    validator = ShadowValidator()
    # Fails gates if Sharpe < 1.0 (currently using defaults)
    # Add two points to make len >= 2
    validator.add_metric_point(0.0001, 0.08)
    validator.add_metric_point(0.0001, 0.08)
    
    report = validator.evaluate_shadow_trading()
    assert report["trading_halted"] is True
