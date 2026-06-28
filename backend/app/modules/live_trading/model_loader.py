import os
import pickle
import logging
from typing import Dict, Any

logger = logging.getLogger("ModelLoader")

class ModelLoader:
    def __init__(self, models_dir: str = "backend/app/modules/prediction/models") -> None:
        self.models_dir = models_dir
        self.model_cache = {}

    def load_production_models(self) -> Dict[str, Dict[str, Any]]:
        """Loads and caches active versions of XGBoost and LSTM models."""
        if not os.path.exists(self.models_dir):
            logger.warning(f"Models directory {self.models_dir} does not exist.")
            return {}

        files = [f for f in os.listdir(self.models_dir) if f.endswith(".pkl")]
        for fn in files:
            # Map names: e.g. XGBoost_1d_...pkl or LSTM_1d_...pkl
            if "XGBoost" in fn:
                key = "xgboost"
            elif "LSTM" in fn:
                key = "lstm"
            else:
                continue

            if key not in self.model_cache:
                path = os.path.join(self.models_dir, fn)
                with open(path, "rb") as f:
                    self.model_cache[key] = pickle.load(f)
                logger.info(f"Loaded production model version for {key}: {fn}")

        return self.model_cache
