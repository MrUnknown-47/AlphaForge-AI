import pytest
from app.modules.shadow_trading.shadow_portfolio import ShadowPortfolio

def test_shadow_portfolio_update():
    portfolio = ShadowPortfolio()
    positions = [
        {"ticker": "AAPL", "quantity": 10.0, "entry_price": 180.0, "market_value": 1800.0, "unrealized_pnl": 0.0}
    ]
    portfolio.update_portfolio_state(10000.0, 11800.0, 10000.0, positions)
    
    assert portfolio.cash == 10000.0
    assert portfolio.portfolio_value == 11800.0
    assert portfolio.positions["AAPL"]["quantity"] == 10.0
    assert abs(portfolio.exposure_pct - (1800.0 / 11800.0)) < 1e-4
