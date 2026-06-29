import pytest
import numpy as np
from app.modules.fund.fund_manager import FundManager
from app.modules.fund.fund_registry import FundRegistry
from app.modules.fund.capital_allocator import CapitalAllocator
from app.modules.fund.fund_constraints import FundConstraintsEvaluator
from app.modules.fund.benchmark_engine import BenchmarkEngine
from app.modules.fund.allocation_engine import CapitalAllocationEngine
from app.modules.fund.risk_budgeting import RiskBudgetingManager
from app.modules.fund.portfolio_builder import PortfolioBuilder
from app.modules.fund.exposure_engine import ExposureEngine
from app.modules.fund.rebalancer import FundRebalancer
from app.modules.fund.scheduler import RebalanceScheduler
from app.modules.fund.execution_planner import ExecutionPlanner
from app.modules.fund.performance_engine import PerformanceEngine
from app.modules.fund.factor_attribution import FactorAttributionEngine
from app.modules.fund.investment_committee import InvestmentCommittee

def test_fund_manager():
    mgr = FundManager()
    assert mgr.nav == 105.42
    mgr.update_nav(0.01) # 1% gain
    assert abs(mgr.nav - 105.42 * 1.01) < 1e-4

def test_fund_registry():
    registry = FundRegistry()
    specs = registry.get_fund_specs("AF_CTA")
    assert specs["benchmark"] == "SG_CTA"

def test_fund_constraints():
    evaluator = FundConstraintsEvaluator()
    check = evaluator.check_constraints(weights={"MOM": 0.35, "REV": 0.20}, leverage=1.50)
    assert check["status"] == "PASSED"

def test_allocation_solvers():
    engine = CapitalAllocationEngine()
    cov = np.array([[0.04, 0.01], [0.01, 0.05]])
    returns = np.array([0.08, 0.12])
    
    erc_w = engine.solve_allocation(returns, cov, method="ERC")
    assert len(erc_w) == 2
    assert abs(np.sum(erc_w) - 1.0) < 1e-4

def test_risk_budgeting():
    rb = RiskBudgetingManager()
    cov = np.array([[0.04, 0.01], [0.01, 0.05]])
    weights = np.array([0.5, 0.5])
    contribs = rb.calculate_marginal_risk_contributions(weights, cov)
    assert len(contribs) == 2
    assert np.all(contribs >= 0)

def test_portfolio_builder():
    builder = PortfolioBuilder()
    cov = np.array([[0.04, 0.01], [0.01, 0.05]])
    returns = np.array([0.08, 0.12])
    port = builder.build_portfolio(["AAPL", "MSFT"], returns, cov, method="ERC")
    assert "AAPL" in port
    assert "MSFT" in port

def test_exposure_engine():
    ee = ExposureEngine()
    weights = {"AAPL": 0.60, "MSFT": 0.40}
    betas = {"AAPL": 1.20, "MSFT": 0.90}
    res = ee.calculate_exposures(weights, betas)
    assert res["gross_exposure"] == 1.0
    assert res["net_exposure"] == 1.0
    assert abs(res["portfolio_beta"] - (0.6 * 1.2 + 0.4 * 0.9)) < 1e-4

def test_rebalancer_and_planner():
    rebalancer = FundRebalancer()
    planner = ExecutionPlanner()
    
    curr = {"AAPL": 0.50, "MSFT": 0.50}
    target = {"AAPL": 0.52, "MSFT": 0.48}
    
    assert not rebalancer.check_drift_and_rebalance(curr, target, threshold=0.05)
    
    orders = planner.generate_rebalance_orders(curr, target, aum=1000000.0)
    assert len(orders) == 2

def test_performance_attribution():
    perf = PerformanceEngine()
    attr = FactorAttributionEngine()
    
    returns = np.array([0.001, -0.002, 0.003])
    bench = np.array([0.0005, -0.001, 0.0015])
    
    metrics = perf.calculate_performance_metrics(returns, bench)
    assert "sharpe_ratio" in metrics
    
    res = attr.attribute_factor_returns(portfolio_return=0.10)
    assert abs(res["market_attribution"] - 0.055) < 1e-4

def test_committee_board():
    ic = InvestmentCommittee()
    res = ic.evaluate_allocations({"MOM": 0.40, "REV": 0.60})
    assert res["decision"] == "APPROVED"
