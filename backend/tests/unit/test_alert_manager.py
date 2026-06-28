import pytest
from app.modules.operations.alert_manager import AlertManager

def test_alert_manager_logging():
    manager = AlertManager()
    alert = manager.trigger_alert("DRAWDOWN_BREACH", "Drawdown limit reached: -15.4%", "CRITICAL")
    
    assert alert["category"] == "DRAWDOWN_BREACH"
    assert alert["severity"] == "CRITICAL"
    assert len(manager.alerts_history) == 1
