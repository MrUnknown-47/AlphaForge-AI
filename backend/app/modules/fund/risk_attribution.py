import numpy as np
from typing import Dict, Any

class RiskAttributionEngine:
    def __init__(self) -> None:
        pass

    def attribute_volatility_contribution(self, weights: np.ndarray, cov: np.ndarray) -> Dict[str, float]:
        """Attributes total portfolio volatility contribution across assets."""
        portfolio_vol = np.sqrt(weights.T.dot(cov).dot(weights))
        if portfolio_vol <= 0:
            return {}
        
        marginal_contrib = cov.dot(weights) / portfolio_vol
        risk_contrib = weights * marginal_contrib
        
        return {
            f"asset_{i}": float(contrib / portfolio_vol) for i, contrib in enumerate(risk_contrib)
        }
