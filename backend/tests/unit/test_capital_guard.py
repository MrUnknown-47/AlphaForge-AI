import pytest
from app.modules.security.capital_guard import CapitalGuard

def test_capital_guardrails():
    guard = CapitalGuard()
    
    # Healthy order
    res_ok = guard.validate_order(order_value=200.0, current_position_value=300.0, current_exposure=0.25)
    assert res_ok["allowed"] is True
    assert res_ok["requires_manual_confirmation"] is False

    # Exceed single order confirmation threshold ($500)
    res_conf = guard.validate_order(order_value=510.0, current_position_value=300.0, current_exposure=0.25)
    assert res_conf["allowed"] is False
    assert res_conf["requires_manual_confirmation"] is True

    # Exceed max position size ($1000)
    res_pos = guard.validate_order(order_value=200.0, current_position_value=900.0, current_exposure=0.25)
    assert res_pos["allowed"] is False
    assert res_pos["reason"] == "POSITION_LIMIT_BREACHED"
