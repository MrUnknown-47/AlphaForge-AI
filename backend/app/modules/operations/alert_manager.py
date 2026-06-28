import logging
from datetime import datetime
from typing import Dict, Any, List

logger = logging.getLogger("AlertManager")

class AlertManager:
    def __init__(self) -> None:
        self.alerts_history: List[Dict[str, Any]] = []

    def trigger_alert(self, category: str, message: str, severity: str = "WARNING") -> Dict[str, Any]:
        alert = {
            "timestamp": datetime.utcnow().isoformat(),
            "category": category,
            "severity": severity,
            "message": message
        }
        self.alerts_history.append(alert)
        logger.warning(f"ALERT [{severity}] ({category}): {message}")
        return alert
