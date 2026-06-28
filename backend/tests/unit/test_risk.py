import pytest
from app.modules.derivatives.risk_engine.service import RiskService

def test_var_cvar_calc():
    returns = [-0.01, -0.02, 0.01, 0.03, -0.05, -0.04, 0.02]
    res = RiskService.calculate_var_cvar(returns, 0.90)
    assert res["var"] > 0.0
    assert res["cvar"] >= res["var"]

def test_stress_test_calc():
    positions = [
        {"quantity": 10, "underlying_price": 100.0, "delta": 0.5, "gamma": 0.02, "vega": 0.15}
    ]
    res = RiskService.perform_stress_tests(positions)
    assert "black_monday_crash" in res
    assert "volatility_crush" in res
