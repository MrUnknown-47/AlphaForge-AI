import numpy as np
from typing import Dict, Any, List
from app.modules.fund.allocation_engine import CapitalAllocationEngine

class PortfolioBuilder:
    def __init__(self) -> None:
        self.allocation_engine = CapitalAllocationEngine()

    def build_portfolio(self, tickers: List[str], expected_returns: np.ndarray, cov: np.ndarray, method: str = "ERC") -> Dict[str, float]:
        weights = self.allocation_engine.solve_allocation(expected_returns, cov, method)
        return dict(zip(tickers, [float(w) for w in weights]))
