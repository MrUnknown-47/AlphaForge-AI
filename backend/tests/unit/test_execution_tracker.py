import pytest
from app.modules.validation.execution_tracker import ExecutionTracker

def test_execution_tracker_metrics():
    tracker = ExecutionTracker()
    log = tracker.log_execution("AAPL", 180.0, 180.18, 12.5, 45.0)
    
    assert log["ticker"] == "AAPL"
    assert abs(log["slippage"] - 0.001) < 1e-4
    assert log["spread_cost"] == 0.00015
    assert log["latency_ms"] == 12.5
    
    metrics = tracker.get_average_metrics()
    assert metrics["avg_latency_ms"] == 12.5
