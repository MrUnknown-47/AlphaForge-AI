from typing import Dict, Any, List

class ModelRegistry:
    def __init__(self) -> None:
        self.models = {
            "AF_GBRT_PRICE_PREDICTOR": {"version": "v2.1.0", "status": "CHAMPION", "accuracy": 0.88},
            "AF_LSTM_VOL_FORECASTER": {"version": "v1.5.0", "status": "CHAMPION", "accuracy": 0.74},
            "AF_RL_CAPITAL_ALLOCATOR": {"version": "v0.9.0-challenger", "status": "CHALLENGER", "accuracy": 0.81}
        }

    def get_models(self) -> Dict[str, Dict[str, Any]]:
        return self.models

    def promote_model(self, name: str) -> None:
        if name in self.models:
            self.models[name]["status"] = "CHAMPION"
