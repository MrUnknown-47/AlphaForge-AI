from typing import Dict, Any, List

class CorporateActionsManager:
    def __init__(self) -> None:
        pass

    def apply_stock_split(self, symbol: str, price: float, quantity: float, ratio: float = 2.0) -> Dict[str, float]:
        """Adjusts price and quantity holding values following a stock split execution."""
        # 2:1 split: double quantity, halve price
        return {
            "adjusted_price": price / ratio,
            "adjusted_quantity": quantity * ratio
        }

    def process_dividend(self, symbol: str, cash_balance: float, dividend_per_share: float, shares_held: float) -> float:
        """Processes cash dividend accruals."""
        payout = shares_held * dividend_per_share
        return cash_balance + payout
