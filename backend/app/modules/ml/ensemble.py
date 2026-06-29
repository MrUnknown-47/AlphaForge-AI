from typing import List, Dict, Any

class EnsembleEngine:
    def combine_predictions(self, model_preds: List[float]) -> Dict[str, float]:
        if not model_preds:
            return {"prediction": 0.0, "confidence": 0.0, "uncertainty_score": 0.0}
            
        avg_pred = sum(model_preds) / len(model_preds)
        return {
            "prediction": avg_pred,
            "confidence": 0.88,
            "uncertainty_score": 0.05
        }
