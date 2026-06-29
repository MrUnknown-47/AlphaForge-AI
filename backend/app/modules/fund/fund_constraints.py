import numpy as np
from typing import Dict, Any

class FundConstraintsEvaluator:
    def __init__(self) -> None:
        self.max_strategy_concentration = 0.40 # max 40% in one strategy
        self.max_portfolio_leverage = 3.0 # max 3.0x leverage ratio

    def check_constraints(self, weights: Dict[str, float], leverage: float) -> Dict[str, Any]:
        """Evaluates strategy allocations and total leverage boundaries."""
        concentration_breach = False
        for strat, weight in weights.items():
            if weight > self.max_strategy_concentration:
                concentration_breach = True
                
        leverage_breach = leverage > self.max_portfolio_leverage
        
        return {
            "concentration_breach": concentration_breach,
            "leverage_breach": leverage_breach,
            "status": "PASSED" if not (concentration_breach or leverage_breach) else "BREACH"
        }
