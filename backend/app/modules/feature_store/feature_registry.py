from typing import Dict, Any, List

class FeatureRegistry:
    def __init__(self) -> None:
        self.catalog = {
            "volatility_20d": {"type": "float", "description": "20-day annualized volatility", "source": "offline"},
            "momentum_10d": {"type": "float", "description": "10-day cross-sectional momentum", "source": "online"},
            "bid_ask_spread_bps": {"type": "float", "description": "Real-time spread in bps", "source": "online"}
        }

    def list_features(self) -> Dict[str, Dict[str, Any]]:
        return self.catalog
