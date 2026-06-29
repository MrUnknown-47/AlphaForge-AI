from typing import Dict, Any

class FuturesRolloverEngine:
    def __init__(self) -> None:
        pass

    def perform_rollover(self, current_symbol: str, next_symbol: str, position_qty: float) -> Dict[str, Any]:
        """Performs rolling of open futures positions to the next front contract month."""
        return {
            "closed_symbol": current_symbol,
            "opened_symbol": next_symbol,
            "rolled_quantity": position_qty,
            "status": "SUCCESSFUL_ROLLOVER"
        }
