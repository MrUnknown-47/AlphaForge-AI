from typing import Dict, Any, List

class StrategyRegistry:
    def __init__(self) -> None:
        self.strategies = {
            "MOMENTUM": {"name": "Cross-Sectional Momentum Strategy", "capacity": 50000000.0, "sharpe": 1.85},
            "MEAN_REVERSION": {"name": "Statistical Arbitrage Mean Reversion", "capacity": 25000000.0, "sharpe": 2.45},
            "TREND_FOLLOWING": {"name": "CTA Trend Following System", "capacity": 100000000.0, "sharpe": 1.15},
            "FACTOR_INVESTING": {"name": "Multi-Factor Quality/Value/Growth", "capacity": 200000000.0, "sharpe": 1.45},
            "MACRO": {"name": "Global Macro Rate Cycles", "capacity": 500000000.0, "sharpe": 1.25}
        }

    def get_strategy(self, key: str) -> Dict[str, Any]:
        return self.strategies.get(key.upper(), {"name": "Generic Strategy", "capacity": 10000000.0, "sharpe": 1.00})
