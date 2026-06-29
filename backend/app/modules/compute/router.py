from fastapi import APIRouter, status
from typing import Dict, Any, List
from app.modules.compute.job_manager import JobManager
from app.modules.compute.cluster_manager import ClusterManager

router = APIRouter(prefix="/compute", tags=["Distributed Compute Service"])
jobs = JobManager()
cluster = ClusterManager()

@router.get("")
async def get_compute_status():
    return {
        "cluster": cluster.get_cluster_specs(),
        "jobs": jobs.list_jobs()
    }

@router.post("/submit", status_code=status.HTTP_202_ACCEPTED)
async def post_submit(job_type: str, payload: Dict[str, Any]):
    job_id = jobs.submit_compute_job(job_type, payload)
    return {"status": "SUBMITTED", "job_id": job_id}
