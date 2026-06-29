from typing import Dict, Any, List

class FuturesExposureTracker:
    def __init__(self) -> None:
        pass

    def calculate_exposure(self, symbol: str, price: float, quantity: float, multiplier: float) -> Dict[str, float]:
        notional = price * abs(quantity) * multiplier
        leverage = notional / (price * abs(quantity)) if quantity != 0 else 0.0
        return {
            "notional_exposure": notional,
            "effective_leverage": leverage
        }
