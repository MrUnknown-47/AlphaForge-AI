import os
import json
import pytest
from app.modules.shadow_validation.monthly_tracker import MonthlyTracker

def test_monthly_validation_logging():
    tracker = MonthlyTracker()
    record = tracker.log_monthly_metrics(
        cagr=0.255, vol=0.14, drawdown=-0.08, pf=1.75, expectancy=0.0015, recovery=2.30, var=-0.012, cvar=-0.018
    )

    assert record["cagr"] == 0.255
    assert record["max_drawdown"] == -0.08
    assert record["recovery_factor"] == 2.30
    assert len(tracker.monthly_records) == 1

    path = os.path.join(tracker.output_dir, "monthly_validation.json")
    assert os.path.exists(path)

    # Clean up test output
    if os.path.exists(path):
        os.remove(path)
