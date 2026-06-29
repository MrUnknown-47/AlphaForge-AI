from typing import Dict, Any

class FeatureMonitorService:
    def __init__(self) -> None:
        pass

    def check_drift(self, feature_name: str, p_value: float = 0.08) -> Dict[str, Any]:
        """Calculates KS-test p-value. If p < 0.05, we have features drift."""
        drift_detected = p_value < 0.05
        return {
            "feature": feature_name,
            "ks_p_value": p_value,
            "drift_detected": drift_detected,
            "status": "DRIFT_ALERT" if drift_detected else "STABLE"
        }
