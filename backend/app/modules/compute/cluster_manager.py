from typing import Dict, Any
from app.modules.compute.workers import ComputeWorkersManager

class ClusterManager:
    def __init__(self) -> None:
        self.workers_mgr = ComputeWorkersManager()

    def get_cluster_specs(self) -> Dict[str, Any]:
        workers = self.workers_mgr.get_workers_status()
        total_cores = sum(w["cores"] for w in workers)
        active_jobs = sum(1 for w in workers if w["status"] == "BUSY")
        return {
            "cluster_id": "alphaforge-ray-cluster",
            "total_nodes": len(workers),
            "total_cores": total_cores,
            "active_jobs_count": active_jobs,
            "status": "ONLINE"
        }
