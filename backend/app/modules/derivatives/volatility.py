import numpy as np
from typing import List

class VolatilityEngine:
    def __init__(self) -> None:
        self.target_volatility = 0.15 # 15% standard target volatility limit

    def calculate_historical_volatility(self, prices: List[float]) -> float:
        if len(prices) < 2:
            return 0.0
        returns = np.diff(prices) / prices[:-1]
        return float(np.std(returns) * np.sqrt(252))

    def calculate_volatility_multiplier(self, current_volatility: float) -> float:
        """Determines leverage multiplier based on volatility targeting (e.g. scale leverage down in high vol regimes)."""
        if current_volatility <= 0:
            return 1.0
        return float(np.clip(self.target_volatility / current_volatility, 0.25, 1.50))
