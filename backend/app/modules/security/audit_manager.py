import os
import json
from datetime import datetime
from typing import Dict, Any, List

class AuditManager:
    def __init__(self, log_dir: str = "backend/app/modules/prediction/reports/security_audit") -> None:
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def log_entry(
        self, username: str, role: str, ip: str, endpoint: str, action: str, details: Dict[str, Any]
    ) -> str:
        timestamp = datetime.utcnow().isoformat()
        log_data = {
            "timestamp": timestamp,
            "user": username,
            "role": role,
            "ip": ip,
            "endpoint": endpoint,
            "action": action,
            "details": details
        }
        
        filename = f"sec_audit_{datetime.utcnow().strftime('%Y%m%d_%H%M%S_%f')}.json"
        path = os.path.join(self.log_dir, filename)
        
        with open(path, "w") as f:
            json.dump(log_data, f, indent=4)
            
        return path
