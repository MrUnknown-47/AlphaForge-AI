import pytest
from app.modules.operations.incident_manager import IncidentManager

def test_incident_classification():
    manager = IncidentManager()
    
    # Classifies broker offline as P0
    inc_p0 = manager.log_incident("BROKER_OFFLINE", "Alpaca REST response timed out")
    assert inc_p0["severity"] == "P0"

    # Classifies Sharpe drop as P1
    inc_p1 = manager.log_incident("SHARPE_DROP", "Rolling Sharpe fell to 0.8")
    assert inc_p1["severity"] == "P1"

    # Classifies websocket reconnects as P2
    inc_p2 = manager.log_incident("WS_RECONNECT", "Reconnected web socket feed")
    assert inc_p2["severity"] == "P2"
