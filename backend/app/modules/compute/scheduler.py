from datetime import datetime
from typing import Dict, Any, List

class ComputeJobScheduler:
    def __init__(self) -> None:
        self.queue: List[Dict[str, Any]] = []

    def submit_job(self, job_id: str, payload: Dict[str, Any]) -> None:
        self.queue.append({
            "job_id": job_id,
            "payload": payload,
            "submitted_at": datetime.utcnow()
        })

    def get_queued_jobs(self) -> List[Dict[str, Any]]:
        return self.queue
