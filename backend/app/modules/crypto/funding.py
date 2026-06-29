from typing import Dict, Any

class CryptoFundingRateManager:
    def __init__(self) -> None:
        pass

    def get_funding_rate(self, symbol: str) -> float:
        """Determines active 8-hour funding rate (simulated)."""
        rates = {
            "BTC-PERP": 0.00012, # 0.012% per 8 hours
            "ETH-PERP": 0.00015,
            "SOL-PERP": 0.00022
        }
        return rates.get(symbol.upper(), 0.00010)

    def calculate_accrued_funding(self, symbol: str, quantity: float, mark_price: float) -> float:
        """Calculates exact dollar payout/charge for holding a perpetual position over the funding mark."""
        rate = self.get_funding_rate(symbol)
        # funding payout = rate * notional
        return rate * quantity * mark_price
