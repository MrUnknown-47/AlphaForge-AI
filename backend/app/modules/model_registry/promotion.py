from typing import Dict, Any
from app.modules.model_registry.registry import ModelRegistry
from app.modules.model_registry.approval import ModelApprovalService

class ModelPromotionWorkflow:
    def __init__(self) -> None:
        self.registry = ModelRegistry()
        self.approval = ModelApprovalService()

    def promote_challenger(self, model_name: str, test_acc: float, champ_acc: float) -> Dict[str, Any]:
        if self.approval.check_promotion_standards(test_acc, champ_acc):
            self.registry.promote_model(model_name)
            return {"model": model_name, "status": "PROMOTED_TO_CHAMPION"}
        return {"model": model_name, "status": "PROMOTION_REJECTED (Low Accuracy)"}
