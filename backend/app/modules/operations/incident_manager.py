import os
import json
from datetime import datetime
from typing import Dict, Any, List

class IncidentManager:
    def __init__(self, output_dir: str = "backend/app/modules/prediction/reports") -> None:
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.incidents: List[Dict[str, Any]] = []

    def log_incident(self, name: str, message: str) -> Dict[str, Any]:
        """
        Classifies incidents:
        P0: broker offline, database offline, drawdown > 20%
        P1: PSI > 0.25, Sharpe < 1, daily loss > 3%
        P2: websocket reconnects, scheduler failures
        """
        name_upper = name.upper()
        severity = "P2"
        
        if "OFFLINE" in name_upper or "DRAWDOWN" in name_upper:
            severity = "P0"
        elif "DRIFT" in name_upper or "PSI" in name_upper or "SHARPE" in name_upper or "LOSS" in name_upper:
            severity = "P1"

        incident = {
            "timestamp": datetime.utcnow().isoformat(),
            "name": name,
            "severity": severity,
            "message": message
        }
        self.incidents.append(incident)
        
        # Save to incident_log.json
        path = os.path.join(self.output_dir, "incident_log.json")
        with open(path, "w") as f:
            json.dump(self.incidents, f, indent=4)

        return incident
