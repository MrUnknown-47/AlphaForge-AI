from typing import Dict, Any

class FeatureValidationService:
    def __init__(self) -> None:
        pass

    def validate_value(self, feature_name: str, value: float) -> bool:
        """Validates feature value bounds to protect models from outlier values."""
        if feature_name == "bid_ask_spread_bps":
            return 0.0 <= value <= 500.0
        return True
