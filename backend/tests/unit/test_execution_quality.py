import pytest
from app.modules.shadow_validation.execution_quality import ExecutionQualityTracker

def test_execution_quality_limits():
    tracker = ExecutionQualityTracker()
    res = tracker.check_execution_quality()
    
    assert res["fill_latency_ms"] == 45.0
    assert res["order_rejection_rate_pct"] == 0.5
    assert res["slippage_bps"] == 4.0
    assert res["quality_check_passed"] is True
