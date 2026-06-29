from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class OpsHealthResponse(BaseModel):
    status: str # GREEN, YELLOW, RED, CRITICAL
    services: Dict[str, str]
    timestamp: datetime

class OpsMetricResponse(BaseModel):
    name: str
    value: float
    timestamp: datetime

class OpsLogResponse(BaseModel):
    message: str
    level: str
    timestamp: datetime

class OpsAlertResponse(BaseModel):
    id: str
    alert_type: str
    message: str
    timestamp: datetime

class OpsIncidentResponse(BaseModel):
    id: str
    severity: str # INFO, WARNING, ERROR, CRITICAL
    message: str
    status: str # ACTIVE, ACKNOWLEDGED, RESOLVED
    timestamp: datetime

class OpsTraceResponse(BaseModel):
    span_id: str
    duration_ms: float

class OpsServiceResponse(BaseModel):
    service_name: str
    status: str
