from typing import List, Dict, Any

class ModelExplainability:
    def get_feature_importances(self) -> List[Dict[str, Any]]:
        return [
            {"feature_name": "returns_1d", "importance": 0.42},
            {"feature_name": "volatility_30d", "importance": 0.28},
            {"feature_name": "pe_ratio", "importance": 0.15}
        ]
