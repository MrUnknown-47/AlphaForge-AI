import pytest
from app.modules.derivatives.futures_engine.service import FuturesStrategyService

def test_directional_pnl():
    res = FuturesStrategyService.directional(2, 5000.0, 5010.0, 0.25, 12.5)
    assert res["strategy"] == "Directional"
    assert res["pnl"] == 1000.0

def test_basis_trading():
    res = FuturesStrategyService.basis_trading(100.0, 102.0, 1.5)
    assert res["basis"] == 2.0
    assert res["arbitrage_pnl"] == 0.5
