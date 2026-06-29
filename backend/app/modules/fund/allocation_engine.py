import numpy as np
from typing import Dict, Any, List
from app.modules.fund.kelly import KellyAllocationSolver
from app.modules.fund.erc import EqualRiskContributionSolver
from app.modules.fund.hrp import HierarchicalRiskParitySolver
from app.modules.fund.black_litterman import BlackLittermanSolver

class CapitalAllocationEngine:
    def __init__(self) -> None:
        self.kelly = KellyAllocationSolver()
        self.erc = EqualRiskContributionSolver()
        self.hrp = HierarchicalRiskParitySolver()
        self.bl = BlackLittermanSolver()

    def solve_allocation(self, expected_returns: np.ndarray, cov: np.ndarray, method: str = "ERC") -> np.ndarray:
        if method == "ERC":
            return self.erc.solve_erc(cov)
        elif method == "HRP":
            return self.hrp.solve_hrp(cov)
        elif method == "KELLY":
            return self.kelly.solve_kelly(expected_returns, cov)
        elif method == "BLACK_LITTERMAN":
            return self.bl.solve_bl(expected_returns, cov)
        return np.ones(len(cov)) / len(cov)
