from typing import Dict, Any

class FuturesContractsManager:
    def __init__(self) -> None:
        self.futures_specs = {
            "ES": {"name": "E-mini S&P 500", "multiplier": 50, "tick_size": 0.25, "currency": "USD"},
            "NQ": {"name": "E-mini Nasdaq 100", "multiplier": 20, "tick_size": 0.25, "currency": "USD"},
            "YM": {"name": "E-mini Dow Jones", "multiplier": 5, "tick_size": 1.00, "currency": "USD"},
            "CL": {"name": "Crude Oil", "multiplier": 1000, "tick_size": 0.01, "currency": "USD"},
            "GC": {"name": "Gold", "multiplier": 100, "tick_size": 0.10, "currency": "USD"},
            "ZN": {"name": "10-Year U.S. Treasury Note", "multiplier": 1000, "tick_size": 0.015625, "currency": "USD"},
            "BTC": {"name": "Bitcoin Futures", "multiplier": 5, "tick_size": 5.00, "currency": "USD"}
        }

    def get_futures_spec(self, symbol: str) -> Dict[str, Any]:
        prefix = symbol.split("_")[0] if "_" in symbol else symbol
        return self.futures_specs.get(prefix.upper(), {"name": "Generic Future", "multiplier": 1, "tick_size": 0.01, "currency": "USD"})
