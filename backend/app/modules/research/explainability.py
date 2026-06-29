from typing import List, Dict

class ModelExplainability:
    def get_shap_values(self) -> List[Dict[str, Any]]:
        return [
            {"feature_name": "Momentum_10d", "shap_value": 0.42},
            {"feature_name": "Volatility_30d", "shap_value": -0.18},
            {"feature_name": "PE_Ratio", "shap_value": 0.25}
        ]
