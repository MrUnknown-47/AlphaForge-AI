import pytest
from app.modules.operations.portfolio_monitor import PortfolioMonitor

def test_portfolio_monitor_eval():
    monitor = PortfolioMonitor()
    res = monitor.evaluate_portfolio(0.45, 1.0, -0.015, -0.022, -0.114)
    
    assert res["exposure"] == 0.45
    assert res["leverage"] == 1.0
    assert res["var_95"] == -0.015
    assert res["cvar_95"] == -0.022
    assert res["drawdown"] == -0.114
    assert res["portfolio_beta"] == 1.05
