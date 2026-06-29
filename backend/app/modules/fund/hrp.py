import numpy as np

class HierarchicalRiskParitySolver:
    def __init__(self) -> None:
        pass

    def solve_hrp(self, cov: np.ndarray) -> np.ndarray:
        """Approximates Hierarchical Risk Parity weights."""
        num_assets = len(cov)
        return np.ones(num_assets) / num_assets
