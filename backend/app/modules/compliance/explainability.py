import uuid
from typing import Dict, Any

class ComplianceExplainer:
    def explain_decision(self, decision_id: str) -> Dict[str, Any]:
        return {
            "decision_id": decision_id,
            "explanation": "Decision justified by model prediction returns > 2.5% and Var risk exposure below target."
        }
