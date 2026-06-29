from typing import Dict, Any, List

class ComputeWorkersManager:
    def __init__(self) -> None:
        self.workers = [
            {"worker_id": "worker_node_0", "status": "BUSY", "cores": 16},
            {"worker_id": "worker_node_1", "status": "IDLE", "cores": 16},
            {"worker_id": "worker_node_2", "status": "IDLE", "cores": 16}
        ]

    def get_workers_status(self) -> List[Dict[str, Any]]:
        return self.workers
