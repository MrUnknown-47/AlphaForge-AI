from typing import Dict, Any

class ContractSpecifications:
    def __init__(self) -> None:
        pass

    def get_notional_value(self, symbol: str, price: float, quantity: float, multiplier: float = 1.0) -> float:
        """Computes the full leveraged notional size of a contract."""
        return price * quantity * multiplier

    def get_initial_margin(self, notional_value: float, margin_requirement: float) -> float:
        """Computes cash capital required to initiate a margin position."""
        return notional_value * margin_requirement
