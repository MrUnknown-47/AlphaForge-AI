import uuid
from datetime import datetime
from typing import List, Dict, Any

class IncidentManager:
    def __init__(self) -> None:
        self.incidents = []

    def create_incident(self, severity: str, message: str) -> Dict[str, Any]:
        incident = {
            "id": str(uuid.uuid4()),
            "severity": severity, # INFO, WARNING, ERROR, CRITICAL
            "message": message,
            "status": "ACTIVE", # ACTIVE, ACKNOWLEDGED, RESOLVED
            "timestamp": datetime.utcnow()
        }
        self.incidents.append(incident)
        return incident

    def acknowledge_incident(self, incident_id: str) -> Dict[str, Any]:
        for inc in self.incidents:
            if inc["id"] == incident_id:
                inc["status"] = "ACKNOWLEDGED"
                return inc
        return {}

    def resolve_incident(self, incident_id: str) -> Dict[str, Any]:
        for inc in self.incidents:
            if inc["id"] == incident_id:
                inc["status"] = "RESOLVED"
                return inc
        return {}
