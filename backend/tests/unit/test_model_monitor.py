import pytest
from app.modules.operations.model_monitor import ModelMonitor

def test_model_monitor_aborts():
    monitor = ModelMonitor()
    
    # Passes validation checks
    res_pass = monitor.track_model_status(1.58, 0.612, 0.85, 0.08)
    assert res_pass["aborted"] is False

    # Violates Sharpe limit (<1.0)
    res_fail_sharpe = monitor.track_model_status(0.8, 0.612, 0.85, 0.08)
    assert res_fail_sharpe["aborted"] is True

    # Violates hit ratio limit (<55%)
    monitor_hr = ModelMonitor()
    res_fail_hr = monitor_hr.track_model_status(1.58, 0.52, 0.85, 0.08)
    assert res_fail_hr["aborted"] is True

    # Violates PSI limit (>0.25)
    monitor_psi = ModelMonitor()
    res_fail_psi = monitor_psi.track_model_status(1.58, 0.612, 0.85, 0.28)
    assert res_fail_psi["aborted"] is True
