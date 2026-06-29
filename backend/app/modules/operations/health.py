from datetime import datetime
from typing import Dict, Any

class HealthMonitor:
    def __init__(self) -> None:
        self.services_status = {
            "database": "GREEN",
            "redis": "GREEN",
            "alpaca_broker": "GREEN",
            "polygon_feed": "GREEN",
            "ml_predictor": "GREEN",
            "ai_agent": "GREEN"
        }

    def get_overall_health(self) -> Dict[str, Any]:
        statuses = list(self.services_status.values())
        if "CRITICAL" in statuses:
            overall = "CRITICAL"
        elif "RED" in statuses:
            overall = "RED"
        elif "YELLOW" in statuses:
            overall = "YELLOW"
        else:
            overall = "GREEN"
            
        return {
            "status": overall,
            "services": self.services_status,
            "timestamp": datetime.utcnow()
        }
        
    def set_service_status(self, service: str, status: str) -> None:
        if service in self.services_status:
            self.services_status[service] = status
