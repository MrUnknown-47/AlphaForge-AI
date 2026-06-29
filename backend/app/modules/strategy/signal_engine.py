from typing import Dict, Any

class SignalEngine:
    def __init__(self) -> None:
        pass

    def compute_signals(self) -> Dict[str, float]:
        """Generates raw trading buy/sell signals for multiple asset classes."""
        return {
            "MOMENTUM": 0.85, # strongly bullish
            "MEAN_REVERSION": -0.12, # slightly bearish/short signal
            "TREND_FOLLOWING": 0.65,
            "FACTOR_INVESTING": 0.45,
            "MACRO": 0.25
        }
