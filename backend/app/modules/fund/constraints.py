import numpy as np
from typing import Dict, Any

class PortfolioConstraintsManager:
    def __init__(self) -> None:
        self.max_exposure = 2.0 # max 200% gross exposure limit
        self.max_turnover = 0.20 # max 20% portfolio turnover limit per rebalance

    def apply_exposure_limits(self, weights: np.ndarray) -> np.ndarray:
        sum_w = np.sum(np.abs(weights))
        if sum_w > self.max_exposure:
            return weights * (self.max_exposure / sum_w)
        return weights
