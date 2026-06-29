from typing import Dict, Any

class FeatureServingService:
    def __init__(self) -> None:
        pass

    def get_online_features(self, entity_id: str) -> Dict[str, float]:
        """Serves real-time online feature vectors for inference."""
        return {
            "entity_id": entity_id,
            "volatility_20d": 0.145,
            "momentum_10d": 0.82,
            "bid_ask_spread_bps": 2.4
        }
