import pytest
from app.modules.derivatives.margin_engine.service import MarginService

def test_reg_t_margin():
    positions = [
        {"type": "STOCK", "quantity": 100, "market_price": 150.0},
        {"type": "OPTION", "quantity": 5, "market_price": 4.5}
    ]
    res = MarginService.calculate_reg_t(positions)
    assert res["portfolio_value"] == 15000.0 + 22.5
    assert res["initial_margin"] == 7500.0 + 22.5

def test_portfolio_margin():
    positions = [
        {"type": "STOCK", "quantity": 100, "underlying_price": 100.0, "market_price": 100.0},
    ]
    res = MarginService.calculate_portfolio_margin(positions)
    assert res["portfolio_value"] == 10000.0
    assert res["initial_margin"] > 0.0
