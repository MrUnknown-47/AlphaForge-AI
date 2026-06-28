import os
import json
import pytest
from app.modules.shadow_validation.weekly_tracker import WeeklyTracker

def test_weekly_validation_logging():
    tracker = WeeklyTracker()
    record = tracker.log_weekly_metrics(
        sharpe=1.65, sortino=2.15, calmar=2.20, vol=0.14, beta=1.02, psi=0.07, conf=0.88
    )

    assert record["rolling_sharpe"] == 1.65
    assert record["rolling_sortino"] == 2.15
    assert record["psi_drift"] == 0.07
    assert len(tracker.weekly_records) == 1

    path = os.path.join(tracker.output_dir, "weekly_validation.json")
    assert os.path.exists(path)

    # Clean up test output
    if os.path.exists(path):
        os.remove(path)
