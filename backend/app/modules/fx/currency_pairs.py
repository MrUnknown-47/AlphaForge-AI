from typing import Dict, Any, List

class CurrencyPairsManager:
    def __init__(self) -> None:
        self.pairs = {
            "EURUSD": {"base": "EUR", "quote": "USD", "pip_decimal": 4},
            "USDJPY": {"base": "USD", "quote": "JPY", "pip_decimal": 2},
            "GBPUSD": {"base": "GBP", "quote": "USD", "pip_decimal": 4},
            "AUDUSD": {"base": "AUD", "quote": "USD", "pip_decimal": 4},
            "USDINR": {"base": "USD", "quote": "INR", "pip_decimal": 4},
            "USDCNH": {"base": "USD", "quote": "CNH", "pip_decimal": 4}
        }

    def get_pair_details(self, symbol: str) -> Dict[str, Any]:
        return self.pairs.get(symbol.upper(), {"base": "USD", "quote": "USD", "pip_decimal": 4})
