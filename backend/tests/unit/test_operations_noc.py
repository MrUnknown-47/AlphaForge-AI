import pytest
from app.modules.operations.health import HealthMonitor
from app.modules.operations.telemetry import TelemetryCollector
from app.modules.operations.incidents import IncidentManager
from app.modules.operations.alerts import AlertEngine
from app.modules.operations.websocket_monitor import OpsWebsocketManager

@pytest.mark.asyncio
async def test_health_states():
    monitor = HealthMonitor()
    
    # 1. Default green check
    res = monitor.get_overall_health()
    assert res["status"] == "GREEN"
    
    # 2. Critical trigger check
    monitor.set_service_status("alpaca_broker", "CRITICAL")
    res_crit = monitor.get_overall_health()
    assert res_crit["status"] == "CRITICAL"

@pytest.mark.asyncio
async def test_telemetry_fields():
    collector = TelemetryCollector()
    metrics = collector.get_system_telemetry()
    
    assert metrics["cpu_pct"] == 34.5
    assert metrics["memory_pct"] == 61.2
    assert metrics["websocket_latency_ms"] == 15.0

@pytest.mark.asyncio
async def test_incident_lifecycle():
    manager = IncidentManager()
    
    # 1. Create incident
    inc = manager.create_incident("ERROR", "Database ping timeout")
    assert inc["severity"] == "ERROR"
    assert inc["status"] == "ACTIVE"
    
    # 2. Acknowledge incident
    ack = manager.acknowledge_incident(inc["id"])
    assert ack["status"] == "ACKNOWLEDGED"
    
    # 3. Resolve incident
    res = manager.resolve_incident(inc["id"])
    assert res["status"] == "RESOLVED"

@pytest.mark.asyncio
async def test_alert_engine():
    engine = AlertEngine()
    alert = engine.trigger_alert("DRIFT_DETECTION", "Model drift metric PSI exceeded")
    
    assert alert["alert_type"] == "DRIFT_DETECTION"
    assert "PSI exceeded" in alert["message"]

@pytest.mark.asyncio
async def test_websocket_broadcast():
    manager = OpsWebsocketManager()
    assert len(manager.active_connections) == 0
