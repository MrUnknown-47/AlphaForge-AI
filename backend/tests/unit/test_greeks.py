import pytest
from app.modules.derivatives.greeks_engine.service import GreeksService

def test_aggregate_greeks():
    positions = [
        {
            "quantity": 10,
            "underlying_price": 100.0,
            "strike": 100.0,
            "expiry_years": 0.25,
            "risk_free_rate": 0.05,
            "implied_volatility": 0.2,
            "option_type": "CALL"
        },
        {
            "quantity": -5,
            "underlying_price": 100.0,
            "strike": 105.0,
            "expiry_years": 0.25,
            "risk_free_rate": 0.05,
            "implied_volatility": 0.22,
            "option_type": "PUT"
        }
    ]
    res = GreeksService.aggregate_portfolio_greeks(positions)
    assert "delta" in res
    assert "gamma" in res
    assert "theta" in res
    assert "vega" in res
    assert "rho" in res
