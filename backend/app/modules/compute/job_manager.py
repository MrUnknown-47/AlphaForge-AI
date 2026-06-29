import uuid
from typing import Dict, Any, List
from app.modules.compute.scheduler import ComputeJobScheduler

class JobManager:
    def __init__(self) -> None:
        self.scheduler = ComputeJobScheduler()
        self.jobs = {
            "job_optuna_hparam": {"type": "BAYESIAN_OPTIMIZATION", "status": "RUNNING", "progress": "65%"},
            "job_fama_french_factor_attribution": {"type": "FACTOR_ATTRIBUTION", "status": "COMPLETED", "progress": "100%"},
            "job_monte_carlo_portfolio_stress": {"type": "MONTE_CARLO_SIMULATION", "status": "QUEUED", "progress": "0%"}
        }

    def list_jobs(self) -> Dict[str, Dict[str, Any]]:
        return self.jobs

    def submit_compute_job(self, job_type: str, payload: Dict[str, Any]) -> str:
        job_id = str(uuid.uuid4())
        self.jobs[job_id] = {"type": job_type, "status": "QUEUED", "progress": "0%"}
        self.scheduler.submit_job(job_id, payload)
        return job_id
