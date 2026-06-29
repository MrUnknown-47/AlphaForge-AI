from typing import Dict, Any

class FuturesMarginEngine:
    def __init__(self) -> None:
        # Standard maintenance margin requirements
        self.maintenance_margins = {
            "ES": 12000.0,
            "NQ": 18000.0,
            "YM": 9500.0,
            "CL": 7500.0,
            "GC": 8500.0,
            "ZN": 2200.0,
            "BTC": 24000.0
        }

    def calculate_margin(self, symbol: str, quantity: float) -> Dict[str, float]:
        prefix = symbol.split("_")[0] if "_" in symbol else symbol
        maint_margin = self.maintenance_margins.get(prefix.upper(), 5000.0) * abs(quantity)
        initial_margin = maint_margin * 1.10 # 110% of maintenance margin
        return {
            "initial_margin": initial_margin,
            "maintenance_margin": maint_margin
        }
