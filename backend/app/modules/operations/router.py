from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect, status
from typing import List, Dict, Any
from datetime import datetime

from app.modules.operations.facade import OperationsFacade
from app.modules.operations.health import HealthMonitor
from app.modules.operations.telemetry import TelemetryCollector
from app.modules.operations.incidents import IncidentManager
from app.modules.operations.alerts import AlertEngine
from app.modules.operations.websocket_monitor import OpsWebsocketManager
from app.modules.operations.schemas import (
    OpsHealthResponse,
    OpsMetricResponse,
    OpsLogResponse,
    OpsAlertResponse,
    OpsIncidentResponse,
    OpsTraceResponse,
    OpsServiceResponse
)

router = APIRouter(prefix="/ops", tags=["Operations Platform Gateway"])

health_monitor = HealthMonitor()
telemetry_collector = TelemetryCollector()
incident_manager = IncidentManager()
alert_engine = AlertEngine()

ws_metrics_manager = OpsWebsocketManager()
ws_logs_manager = OpsWebsocketManager()
ws_alerts_manager = OpsWebsocketManager()
ws_incidents_manager = OpsWebsocketManager()
ws_health_manager = OpsWebsocketManager()

def get_ops_facade() -> OperationsFacade:
    return OperationsFacade()

@router.get("/health", response_model=OpsHealthResponse)
async def get_ops_health():
    res = health_monitor.get_overall_health()
    return res

@router.get("/metrics", response_model=List[OpsMetricResponse])
async def get_ops_metrics():
    tel = telemetry_collector.get_system_telemetry()
    return [
        {"name": "cpu_pct", "value": tel["cpu_pct"], "timestamp": datetime.utcnow()},
        {"name": "memory_pct", "value": tel["memory_pct"], "timestamp": datetime.utcnow()},
        {"name": "api_latency_ms", "value": tel["api_latency_ms"], "timestamp": datetime.utcnow()}
    ]

@router.get("/logs", response_model=List[OpsLogResponse])
async def get_ops_logs():
    return [
        {"message": "Database reconnection check success.", "level": "INFO", "timestamp": datetime.utcnow()},
        {"message": "Broker websocket reconnecting...", "level": "WARNING", "timestamp": datetime.utcnow()}
    ]

@router.get("/alerts", response_model=List[OpsAlertResponse])
async def get_ops_alerts_list():
    return [
        {"id": a["id"], "alert_type": a["alert_type"], "message": a["message"], "timestamp": a["timestamp"]}
        for a in alert_engine.alerts
    ] or [
        {"id": "ALERT_MOCK_1", "alert_type": "WEBSOCKET_DROP", "message": "Polygon websocket feed disconnected.", "timestamp": datetime.utcnow()}
    ]

@router.get("/incidents", response_model=List[OpsIncidentResponse])
async def get_ops_incidents_list():
    return [
        {"id": i["id"], "severity": i["severity"], "message": i["message"], "status": i["status"], "timestamp": i["timestamp"]}
        for i in incident_manager.incidents
    ] or [
        {"id": "INCIDENT_MOCK_1", "severity": "ERROR", "message": "Database query latency exceeded 500ms threshold.", "status": "ACTIVE", "timestamp": datetime.utcnow()}
    ]

@router.get("/traces", response_model=List[OpsTraceResponse])
async def get_ops_traces():
    return [
        {"span_id": "span_fetch_quotes", "duration_ms": 142.5},
        {"span_id": "span_compute_var", "duration_ms": 32.8}
    ]

@router.get("/services", response_model=List[OpsServiceResponse])
async def get_ops_services():
    health_data = health_monitor.get_overall_health()
    return [
        {"service_name": name, "status": stat}
        for name, stat in health_data["services"].items()
    ]

@router.post("/alert")
async def create_alert(alert_type: str, message: str):
    res = alert_engine.trigger_alert(alert_type, message)
    await ws_alerts_manager.broadcast(f"New Alert: {message}")
    return res

@router.post("/incident")
async def create_incident(severity: str, message: str):
    res = incident_manager.create_incident(severity, message)
    await ws_incidents_manager.broadcast(f"New Incident: [{severity}] {message}")
    return res

@router.post("/acknowledge")
async def acknowledge_incident(incident_id: str):
    res = incident_manager.acknowledge_incident(incident_id)
    return res

@router.post("/kill-switch")
async def toggle_kill_switch(active: bool):
    health_monitor.set_service_status("alpaca_broker", "CRITICAL" if active else "GREEN")
    return {"status": "SUCCESS", "kill_switch_active": active}

# Websockets Routes
@router.websocket("/ws/metrics")
async def ws_metrics_endpoint(websocket: WebSocket):
    await ws_metrics_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_metrics_manager.disconnect(websocket)

@router.websocket("/ws/logs")
async def ws_logs_endpoint(websocket: WebSocket):
    await ws_logs_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_logs_manager.disconnect(websocket)

@router.websocket("/ws/alerts")
async def ws_alerts_endpoint(websocket: WebSocket):
    await ws_alerts_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_alerts_manager.disconnect(websocket)

@router.websocket("/ws/incidents")
async def ws_incidents_endpoint(websocket: WebSocket):
    await ws_incidents_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_incidents_manager.disconnect(websocket)

@router.websocket("/ws/health")
async def ws_health_endpoint(websocket: WebSocket):
    await ws_health_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_health_manager.disconnect(websocket)
