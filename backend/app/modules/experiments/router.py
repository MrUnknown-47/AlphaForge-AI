from fastapi import APIRouter, status
from typing import Dict, Any, List
from app.modules.experiments.experiment_manager import ExperimentManager
from app.modules.experiments.comparison import ExperimentComparison

router = APIRouter(prefix="/experiments", tags=["Experiment Tracking Service"])
mgr = ExperimentManager()
comparison = ExperimentComparison()

@router.get("")
async def list_experiments():
    return mgr.list_experiments()

@router.post("/run", status_code=status.HTTP_201_CREATED)
async def post_run(name: str, parameters: Dict[str, Any], metrics: Dict[str, Any]):
    mgr.log_trial(name, parameters, metrics)
    return {"status": "LOGGED", "name": name}

@router.get("/compare")
async def get_compare(run_a_name: str, run_b_name: str):
    exps = mgr.list_experiments()
    run_a = exps.get(run_a_name, {})
    run_b = exps.get(run_b_name, {})
    return comparison.compare_runs(run_a, run_b)
