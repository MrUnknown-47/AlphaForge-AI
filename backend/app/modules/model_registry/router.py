from fastapi import APIRouter, status
from typing import Dict, Any, List
from app.modules.model_registry.registry import ModelRegistry
from app.modules.model_registry.promotion import ModelPromotionWorkflow
from app.modules.model_registry.rollback import ModelRollbackService

router = APIRouter(prefix="/models", tags=["Model Registry Service"])
registry = ModelRegistry()
promoter = ModelPromotionWorkflow()
rollbacker = ModelRollbackService()

@router.get("")
async def list_models():
    return registry.get_models()

@router.post("/promote", status_code=status.HTTP_200_OK)
async def post_promote(model_name: str, test_accuracy: float, champion_accuracy: float):
    res = promoter.promote_challenger(model_name, test_accuracy, champion_accuracy)
    return res

@router.post("/rollback", status_code=status.HTTP_200_OK)
async def post_rollback(model_name: str, previous_version: str):
    res = rollbacker.rollback_model_version(model_name, previous_version)
    return res
