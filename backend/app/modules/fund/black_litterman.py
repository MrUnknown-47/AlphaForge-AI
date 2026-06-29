import numpy as np

class BlackLittermanSolver:
    def __init__(self) -> None:
        pass

    def solve_bl(self, expected_returns: np.ndarray, cov: np.ndarray) -> np.ndarray:
        """Solves Black-Litterman implied weights representation."""
        inv_cov = np.linalg.pinv(cov)
        weights = inv_cov.dot(expected_returns * 1.05)
        sum_w = np.sum(weights)
        if sum_w > 0:
            return weights / sum_w
        return np.ones(len(cov)) / len(cov)
