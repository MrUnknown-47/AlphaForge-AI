from typing import Dict, Any

class CryptoRiskEngine:
    def __init__(self) -> None:
        pass

    def calculate_liquidation_price(self, entry_price: float, leverage: float, is_long: bool) -> float:
        """Calculates exact liquidation boundary price based on leverage multiplier."""
        # Simplified formula: liquidation price = entry * (1 - 1/leverage) for long, entry * (1 + 1/leverage) for short
        if leverage <= 0:
            return 0.0
        
        offset = entry_price / leverage
        if is_long:
            return float(entry_price - offset)
        else:
            return float(entry_price + offset)
