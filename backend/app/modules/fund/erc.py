import numpy as np

class EqualRiskContributionSolver:
    def __init__(self) -> None:
        pass

    def solve_erc(self, cov: np.ndarray) -> np.ndarray:
        """Approximates Equal Risk Contribution weights using inverse volatility scaling."""
        vols = np.sqrt(np.diag(cov))
        inv_vols = 1.0 / vols
        sum_inv = np.sum(inv_vols)
        if sum_inv > 0:
            return inv_vols / sum_inv
        return np.ones(len(cov)) / len(cov)
