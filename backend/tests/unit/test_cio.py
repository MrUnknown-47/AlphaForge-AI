import pytest
import numpy as np
from app.modules.portfolio_optimization.optimizer import PortfolioOptimizer
from app.modules.portfolio_optimization.constraints import PortfolioConstraints
from app.modules.portfolio_optimization.risk_models import RiskModel
from app.modules.portfolio_optimization.rebalance import PortfolioRebalancer
from app.modules.cio.chief_investment_officer import ChiefInvestmentOfficer
from app.modules.derivatives.options_engine import OptionsEngine
from app.modules.derivatives.greeks import GreeksMonitor

@pytest.mark.asyncio
async def test_portfolio_optimizers():
    opt = PortfolioOptimizer()
    returns = np.array([0.10, 0.12])
    cov = np.array([[0.04, 0.01], [0.01, 0.05]])
    
    mvo_w = opt.mean_variance_optimization(returns, cov)
    assert len(mvo_w) == 2
    assert np.all(mvo_w >= 0.0)
    assert np.all(mvo_w <= 1.0)
    
    parity_w = opt.risk_parity(cov)
    assert len(parity_w) == 2
    assert abs(np.sum(parity_w) - 1.0) < 1e-4

def test_portfolio_constraints():
    constraints = PortfolioConstraints()
    # Use 5 assets so it is mathematically possible to normalize to 1.0 with <= 0.25 individual limits
    raw = np.array([0.30, 0.30, 0.20, 0.10, 0.10])
    w = constraints.apply_constraints(raw)
    assert np.all(w <= 0.25)
    assert abs(np.sum(w) - 1.0) < 1e-4

def test_risk_model_shrinkage():
    rm = RiskModel()
    returns_data = np.random.randn(100, 3)
    shrunk_cov = rm.ledoit_wolf_shrinkage(returns_data)
    assert shrunk_cov.shape == (3, 3)

def test_rebalance_trigger():
    rebalancer = PortfolioRebalancer()
    curr = {"AAPL": 0.20, "NVDA": 0.25}
    target = {"AAPL": 0.22, "NVDA": 0.23}
    
    # 1. No drift trigger
    assert not rebalancer.evaluate_rebalance_trigger(curr, target, drawdown=0.01, volatility=0.15)
    
    # 2. Drawdown trigger
    assert rebalancer.evaluate_rebalance_trigger(curr, target, drawdown=-0.08, volatility=0.15)

@pytest.mark.asyncio
async def test_cio_cycle():
    cio = ChiefInvestmentOfficer()
    returns_data = np.random.randn(100, 3)
    res = await cio.run_allocation_cycle(["AAPL", "NVDA", "MSFT"], returns_data)
    assert "optimized_allocation" in res
    assert "committee_decisions" in res
    assert "stress_tests" in res
    assert "explanations" in res

def test_options_greeks():
    engine = OptionsEngine()
    # Call BS Greeks
    res = engine.black_scholes_greeks(spot=100.0, strike=100.0, time_to_expiry=30.0/365.0, rate=0.04, vol=0.20, o_type="call")
    assert "price" in res
    assert 0.45 < res["delta"] < 0.65
    assert res["gamma"] > 0
    assert res["vega"] > 0
