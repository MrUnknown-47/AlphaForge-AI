from fastapi import APIRouter, status
from typing import Dict, Any, List
from app.modules.feature_store.feature_registry import FeatureRegistry
from app.modules.feature_store.feature_serving import FeatureServingService
from app.modules.feature_store.feature_monitor import FeatureMonitorService

router = APIRouter(prefix="/features", tags=["Feature Store Service"])
registry = FeatureRegistry()
serving = FeatureServingService()
monitor = FeatureMonitorService()

@router.get("")
async def list_features():
    return registry.list_features()

@router.get("/serving/{entity_id}")
async def get_serving(entity_id: str):
    return serving.get_online_features(entity_id)

@router.get("/monitor/{feature_name}")
async def get_monitor(feature_name: str):
    return monitor.check_drift(feature_name)