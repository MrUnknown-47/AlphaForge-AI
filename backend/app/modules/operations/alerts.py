import uuid
from datetime import datetime
from typing import List, Dict, Any

class AlertEngine:
    def __init__(self) -> None:
        self.alerts = []

    def trigger_alert(self, alert_type: str, message: str) -> Dict[str, Any]:
        alert = {
            "id": str(uuid.uuid4()),
            "alert_type": alert_type,
            "message": message,
            "timestamp": datetime.utcnow()
        }
        self.alerts.append(alert)
        return alert
