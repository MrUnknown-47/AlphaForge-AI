import pytest
from app.modules.derivatives.pricing_engine.black_scholes import (
    call_price, put_price, implied_volatility, delta, gamma, theta, vega, rho
)

def test_pricing_options():
    c_val = call_price(100.0, 100.0, 1.0, 0.05, 0.20)
    p_val = put_price(100.0, 100.0, 1.0, 0.05, 0.20)
    
    assert c_val > 0.0
    assert p_val > 0.0
    
    # Check IV estimation
    iv_call = implied_volatility(c_val, 100.0, 100.0, 1.0, 0.05)
    assert abs(iv_call - 0.20) < 0.01

def test_greeks_calculations():
    S, K, T, r, sigma = 100.0, 100.0, 1.0, 0.05, 0.20
    assert 0.0 < delta(S, K, T, r, sigma, "CALL") < 1.0
    assert -1.0 < delta(S, K, T, r, sigma, "PUT") < 0.0
    assert gamma(S, K, T, r, sigma) > 0.0
    assert vega(S, K, T, r, sigma) > 0.0
    assert theta(S, K, T, r, sigma, "CALL") < 0.0
    assert rho(S, K, T, r, sigma, "CALL") > 0.0
