import pytest
from app.modules.live_trading.telemetry import calculate_slippage_bps, calculate_implementation_shortfall, calculate_market_impact
from app.modules.live_trading.pnl_engine import LivePnlEngine
from app.modules.live_trading.risk_monitor import LiveRiskMonitor
from app.modules.live_trading.execution_monitor import ExecutionMonitor

@pytest.mark.asyncio
async def test_telemetry_calculations():
    # 1. Slippage bps (5 cents on 150 dollars)
    bps = calculate_slippage_bps(arrival_price=150.0, fill_price=150.05, side="BUY")
    assert bps == pytest.approx(3.333, abs=1e-3)
    
    # 2. Implementation Shortfall
    is_val = calculate_implementation_shortfall(decision_price=150.0, fill_price=150.05, quantity=100.0, fees=2.5)
    assert is_val == pytest.approx(7.5)
    
    # 3. Market impact
    impact = calculate_market_impact(qty=100.0, daily_volume=1000000.0, vol_pct=0.02)
    assert impact >= 0.0

@pytest.mark.asyncio
async def test_pnl_updates():
    engine = LivePnlEngine()
    positions = [
        {"symbol": "AAPL", "quantity": 10, "entry_price": 150.0, "market_price": 160.0, "market_value": 1600.0, "unrealized_pnl": 100.0}
    ]
    res = engine.update_pnl(positions, cash=98500.0) # Total equity = 1600 + 98500 = 100100
    
    assert res["running_equity"] == 100100.0
    assert res["unrealized_pnl"] == 100.0
    assert res["daily_pnl"] == 100.0

@pytest.mark.asyncio
async def test_risk_controls():
    risk = LiveRiskMonitor()
    
    # 1. Kill Switch Active
    risk.set_kill_switch(True)
    assert risk.kill_switch_active is True

    # 2. Normal order check
    assert risk.check_pre_trade_limits("AAPL", quantity=1.0, price=150.0, portfolio_val=100000.0, active_positions=[]) is True

    # 3. Initialize baseline
    risk.check_post_trade_limits(portfolio_val=100000.0)
    
    # 4. Breaches checking (breaching daily loss limits)
    alerts = risk.check_post_trade_limits(portfolio_val=95000.0) # Down 5% (limit is 3%)
    assert len(alerts) > 0
    assert "breached" in alerts[0]
