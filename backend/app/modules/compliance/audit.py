import hashlib
import uuid
from datetime import datetime
from typing import Dict, Any

class ComplianceAuditLogger:
    def __init__(self) -> None:
        self.last_hash = "0" * 64

    def log_action(self, action: str, actor_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        timestamp = datetime.utcnow().isoformat()
        raw_str = f"{action}|{actor_id}|{timestamp}|{self.last_hash}"
        new_hash = hashlib.sha256(raw_str.encode()).hexdigest()
        self.last_hash = new_hash
        
        return {
            "id": str(uuid.uuid4()),
            "action": action,
            "actor_id": actor_id,
            "timestamp": datetime.utcnow(),
            "hash": new_hash
        }
