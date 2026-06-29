import numpy as np
from typing import List, Dict, Any
from app.modules.portfolio_optimization.optimizer import PortfolioOptimizer
from app.modules.portfolio_optimization.constraints import PortfolioConstraints
from app.modules.portfolio_optimization.risk_models import RiskModel

class CapitalAllocationEngine:
    def __init__(self) -> None:
        self.optimizer = PortfolioOptimizer()
        self.constraints = PortfolioConstraints()
        self.risk_model = RiskModel()

    def generate_allocations(self, tickers: List[str], returns_data: np.ndarray, method: str = "MVO") -> Dict[str, float]:
        num_assets = len(tickers)
        if num_assets == 0:
            return {}

        expected_returns = np.mean(returns_data, axis=0)
        cov = self.risk_model.ledoit_wolf_shrinkage(returns_data)

        if method == "MVO":
            w = self.optimizer.mean_variance_optimization(expected_returns, cov)
        elif method == "RISK_PARITY":
            w = self.optimizer.risk_parity(cov)
        else:
            w = np.ones(num_assets) / num_assets

        # Apply portfolio constraints
        w = self.constraints.apply_constraints(w)
        
        return dict(zip(tickers, [float(x) for x in w]))
