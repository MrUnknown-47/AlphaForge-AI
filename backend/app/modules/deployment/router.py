from fastapi import APIRouter, status
from typing import Dict, Any, List
from app.modules.deployment.deployment_manager import DeploymentManager
from app.modules.deployment.release_manager import ReleaseManager
from app.modules.deployment.rollback_manager import RollbackManager
from app.modules.deployment.health_checker import HealthChecker

router = APIRouter(prefix="/deployment", tags=["Deployment & Release Service"])
deployer = DeploymentManager()
releaser = ReleaseManager()
rollbacker = RollbackManager()
health = HealthChecker()

@router.get("")
async def get_deployments():
    return deployer.get_deployments()

@router.get("/health")
async def get_health():
    return health.run_health_checks()

@router.post("/release", status_code=status.HTTP_201_CREATED)
async def post_release(version: str, environment: str):
    releaser.approve_release(version)
    res = deployer.deploy_new_version(version, environment)
    return res

@router.post("/rollback", status_code=status.HTTP_200_OK)
async def post_rollback(current_version: str, target_version: str):
    res = rollbacker.execute_rollback(current_version, target_version)
    return res
