import numpy as np

class RiskModel:
    def __init__(self) -> None:
        pass

    def ledoit_wolf_shrinkage(self, price_returns: np.ndarray, shrinkage_factor: float = 0.15) -> np.ndarray:
        """Ledoit-Wolf shrinkage to regularize covariance matrices for unstable weights solver."""
        cov = np.cov(price_returns, rowvar=False)
        num_assets = cov.shape[0]
        # Target diagonal matrix
        target = np.diag(np.diag(cov))
        # Shrinkage model
        shrunk_cov = (1 - shrinkage_factor) * cov + shrinkage_factor * target
        return shrunk_cov
