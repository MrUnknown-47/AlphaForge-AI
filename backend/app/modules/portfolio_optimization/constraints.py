import numpy as np

class PortfolioConstraints:
    def __init__(self) -> None:
        self.max_position_size = 0.25 # max 25% in one asset
        self.max_sector_exposure = 0.40 # max 40% in one sector
        self.max_leverage = 1.50 # max 1.5x leverage
        self.max_turnover = 0.15 # max 15% rebalance turnover limit
        self.min_liquidity_days = 5

    def apply_constraints(self, target_weights: np.ndarray, current_weights: np.ndarray = None) -> np.ndarray:
        """Applies limit clipping bounds iteratively to satisfy normalization sum of 1.0 and bounds <= 0.25."""
        w = target_weights.copy()
        
        # Iteratively normalize and clip to resolve bounds conflict
        for _ in range(30):
            sum_w = np.sum(w)
            if sum_w > 0:
                w = w / sum_w
            w = np.clip(w, 0.0, self.max_position_size)

        return w
