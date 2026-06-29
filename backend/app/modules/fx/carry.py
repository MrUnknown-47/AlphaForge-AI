from typing import Dict, Any

class ForexCarryCalculator:
    def __init__(self) -> None:
        # Annual central bank rates
        self.interest_rates = {
            "USD": 0.0525,
            "EUR": 0.0425,
            "GBP": 0.0500,
            "JPY": 0.0025,
            "AUD": 0.0435,
            "INR": 0.0650,
            "CNH": 0.0200
        }

    def calculate_carry_rate(self, pair: str, is_long: bool) -> float:
        """Calculates long or short interest rate differential (annualized carry rate)."""
        base = pair[:3]
        quote = pair[3:]
        base_rate = self.interest_rates.get(base, 0.02)
        quote_rate = self.interest_rates.get(quote, 0.02)
        
        # Long base currency means buying base, borrowing quote
        # Short base currency means borrowing base, buying quote
        if is_long:
            return float(base_rate - quote_rate)
        else:
            return float(quote_rate - base_rate)
