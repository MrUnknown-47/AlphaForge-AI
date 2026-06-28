import pytest
from app.modules.operations.uptime_tracker import UptimeTracker
from app.modules.operations.health_monitor import HealthMonitor

def test_health_monitor_ticks():
    tracker = UptimeTracker()
    monitor = HealthMonitor(tracker)
    
    # 2 failed out of 1000 ticks = 99.8% uptime
    res = monitor.check_health()
    assert res["api_uptime"] == 99.8
    assert res["polygon_connected"] is True
    assert res["alpaca_connected"] is True
