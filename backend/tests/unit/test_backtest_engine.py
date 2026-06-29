import pytest
from app.modules.backtesting.engine import EventDrivenBacktestEngine, MarketEvent, SignalEvent
from app.modules.backtesting.simulator import BrokerSimulator
from app.modules.backtesting.statistics import calculate_sharpe, calculate_sortino, calculate_max_drawdown, calculate_omega
from app.modules.backtesting.montecarlo import MonteCarloSimulator
from app.modules.backtesting.walkforward import WalkForwardOptimizer

@pytest.mark.asyncio
async def test_event_driven_queue():
    engine = EventDrivenBacktestEngine()
    
    # 1. Enqueue market tick
    engine.event_queue.put(MarketEvent("2026-06-28T10:00:00", "AAPL", 150.0, 152.0, 149.0, 151.0, 10000.0))
    # 2. Enqueue signal
    engine.event_queue.put(SignalEvent("AAPL", "2026-06-28T10:00:00", "BUY", 0.95))
    
    # 3. Run event loop
    engine.run()
    assert len(engine.trades) > 0
    assert engine.trades[0]["symbol"] == "AAPL"

@pytest.mark.asyncio
async def test_broker_simulation():
    sim = BrokerSimulator(commission_rate=0.001, slippage_pct=0.0005)
    res = sim.execute_order(order_type="MARKET", qty=10.0, price=150.0, side="BUY")
    
    # Buy price with slippage: 150.0 * (1 + 0.0005) = 150.075
    assert res["fill_price"] == 150.075
    # Commission: 150.075 * 10 * 0.001 = 1.50075
    assert res["commission"] == pytest.approx(1.50075)

@pytest.mark.asyncio
async def test_backtest_statistics():
    returns = [0.01, -0.015, 0.02, -0.005, 0.012]
    equity_curve = [100000.0, 101000.0, 99485.0, 101474.0, 100966.0, 102178.0]
    
    sharpe = calculate_sharpe(returns)
    sortino = calculate_sortino(returns)
    max_dd = calculate_max_drawdown(equity_curve)
    omega = calculate_omega(returns)
    
    assert sharpe >= 0.0
    assert sortino >= 0.0
    assert max_dd == pytest.approx(0.015, abs=1e-5) # Drop from 101000 to 99485 is 1515/101000 = 0.015

@pytest.mark.asyncio
async def test_monte_carlo():
    mc = MonteCarloSimulator(num_simulations=100)
    res = mc.run_simulation(historical_returns=[0.01, -0.01, 0.02, -0.015], initial_equity=100.0, periods=10)
    
    assert res["ruin_probability"] >= 0.0
    assert len(res["confidence_bands_95"]) == 2

@pytest.mark.asyncio
async def test_walk_forward():
    wf = WalkForwardOptimizer(train_ratio=0.7)
    res = wf.run_optimization(
        data=[{"close": 150.0}, {"close": 152.0}, {"close": 151.0}],
        parameters_grid=[{"ma": 10}, {"ma": 20}]
    )
    assert res["best_parameters"] == {"ma": 10}
