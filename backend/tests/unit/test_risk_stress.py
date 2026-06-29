import pytest
from app.modules.risk.var import calculate_parametric_var, calculate_historical_var
from app.modules.risk.cvar import calculate_cvar
from app.modules.risk.stress import StressTestingEngine
from app.modules.risk.liquidity import LiquidityRiskEngine
from app.modules.risk.limits import RiskLimitsManager

@pytest.mark.asyncio
async def test_var_computations():
    returns = [0.01, -0.02, 0.03, 0.015, -0.005]
    
    var_p = calculate_parametric_var(returns, 0.95)
    assert var_p >= 0.0
    
    var_h = calculate_historical_var(returns, 0.95)
    assert var_h >= 0.0

@pytest.mark.asyncio
async def test_cvar_shortfall():
    returns = [0.01, -0.02, 0.03, -0.05, 0.015, -0.005, -0.01, -0.015, -0.03, -0.04]
    cvar = calculate_cvar(returns, 0.95)
    assert cvar >= 0.0

@pytest.mark.asyncio
async def test_stress_scenarios():
    engine = StressTestingEngine()
    res = engine.evaluate_scenario("Black Monday 1987", portfolio_value=100000.0)
    
    assert res["scenario_name"] == "Black Monday 1987"
    assert res["portfolio_loss"] == 22600.0 # 22.6% of 100000
    assert res["expected_drawdown"] == 0.30
    assert res["recovery_time_months"] == 18

@pytest.mark.asyncio
async def test_liquidity_horizon():
    engine = LiquidityRiskEngine()
    res = engine.calculate_liquidity_risk("AAPL", quantity=1000.0, daily_volume=100000.0)
    
    assert res["symbol"] == "AAPL"
    assert res["bid_ask_spread_pct"] == 0.0005
    assert res["liquidation_horizon_days"] == pytest.approx(0.1) # 1000 / (100000 * 0.1) = 0.1

@pytest.mark.asyncio
async def test_risk_limits_triggers():
    manager = RiskLimitsManager(max_drawdown=0.10)
    
    # 1. Normal state (drawdown 2% < limit 10%)
    res_normal = manager.evaluate_drawdown(0.02)
    assert res_normal["limit_breached"] is False
    assert res_normal["action_required"] == "NONE"
    
    # 2. Reduce state (drawdown 8% > limit 7%)
    res_reduce = manager.evaluate_drawdown(0.08)
    assert res_reduce["limit_breached"] is False
    assert res_reduce["action_required"] == "REDUCE"
    
    # 3. Liquidate state (drawdown 12% > limit 10%)
    res_liq = manager.evaluate_drawdown(0.12)
    assert res_liq["limit_breached"] is True
    assert res_liq["action_required"] == "LIQUIDATE"
    assert manager.kill_switch_active is True
