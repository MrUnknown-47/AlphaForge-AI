import os
import json
import pytest
from app.modules.shadow_validation.daily_tracker import DailyTracker

def test_daily_validation_logging():
    tracker = DailyTracker()
    record = tracker.log_daily_metrics(
        realized=120.0, unrealized=50.0, trades=4, hit_ratio=0.75,
        holding_time=2.8, exposure=0.35, slippage=0.0004, tx_cost=10.0
    )
    
    assert record["realized_pnl"] == 120.0
    assert record["unrealized_pnl"] == 50.0
    assert record["trade_count"] == 4
    assert record["slippage_bps"] == 4.0
    assert len(tracker.daily_records) == 1

    path = os.path.join(tracker.output_dir, "daily_validation.json")
    assert os.path.exists(path)

    # Clean up test output
    if os.path.exists(path):
        os.remove(path)
