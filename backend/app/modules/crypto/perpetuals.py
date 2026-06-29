from typing import Dict, Any

class CryptoPerpetualsManager:
    def __init__(self) -> None:
        pass

    def calculate_notional_perps(self, mark_price: float, quantity: float, leverage: float = 10.0) -> Dict[str, float]:
        """Calculates margin required and position notional for leveraged perpetuals contracts."""
        notional = mark_price * abs(quantity)
        margin_required = notional / leverage
        return {
            "position_notional": notional,
            "margin_required": margin_required,
            "effective_leverage": leverage
        }
