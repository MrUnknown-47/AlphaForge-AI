import logging
from typing import Dict, Any

logger = logging.getLogger("ModelRollback")

class ModelRollbackService:
    def __init__(self) -> None:
        pass

    def rollback_model_version(self, model_name: str, previous_version: str) -> Dict[str, Any]:
        logger.warning(f"MODEL ROLLBACK: rolling back {model_name} to stable version: {previous_version}")
        return {
            "model": model_name,
            "rolled_back_to": previous_version,
            "status": "ROLLBACK_COMPLETE"
        }
