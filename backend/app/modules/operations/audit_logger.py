import os
import json
import logging
from datetime import datetime
from typing import Dict, Any, List

logger = logging.getLogger("AuditLogger")

class AuditLogger:
    def __init__(self, log_dir: str = "backend/app/modules/prediction/reports/audit") -> None:
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def log_action(self, component: str, payload: Dict[str, Any]) -> str:
        """Appends immutable JSON records to chronological audit files."""
        timestamp = datetime.utcnow().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "component": component,
            "payload": payload
        }
        
        # Save to individual audit file named by timestamp
        filename = f"audit_{datetime.utcnow().strftime('%Y%m%d_%H%M%S_%f')}.json"
        path = os.path.join(self.log_dir, filename)
        
        with open(path, "w") as f:
            json.dump(log_entry, f, indent=4)
            
        logger.info(f"Immutable audit entry written to: {path}")
        return path
