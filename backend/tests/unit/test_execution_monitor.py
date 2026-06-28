import pytest
from app.modules.shadow_trading.execution_monitor import ExecutionMonitor

def test_execution_monitor_averages():
    monitor = ExecutionMonitor()
    monitor.log_execution("AAPL", 180.0, 180.09, 120.0, rejected=False) # 5 bps slippage
    monitor.log_execution("MSFT", 400.0, 400.0, 180.0, rejected=True) # rejected
    
    stats = monitor.get_summary_stats()
    assert abs(stats["average_slippage"] - 0.0005) < 1e-4
    assert stats["median_latency"] == 150.0
    assert stats["fill_percentage"] == 50.0
