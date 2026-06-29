import numpy as np

class KellyAllocationSolver:
    def __init__(self) -> None:
        pass

    def solve_kelly(self, expected_returns: np.ndarray, cov: np.ndarray, fraction: float = 0.5) -> np.ndarray:
        """Solves optimal Kelly fractional leverage allocation weights."""
        inv_cov = np.linalg.pinv(cov)
        weights = inv_cov.dot(expected_returns) * fraction
        # clip to prevent massive short positions
        return np.clip(weights, -1.0, 1.0)
