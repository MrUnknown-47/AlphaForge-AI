from typing import Dict, Any

class AlphaAttributionEngine:
    def __init__(self) -> None:
        pass

    def attribute_alpha_contribution(self, strategy_weights: Dict[str, float], strategy_alphas: Dict[str, float]) -> Dict[str, float]:
        """Calculates alpha contributions for each strategy based on weights and alpha values."""
        contribution = {}
        for strat, weight in strategy_weights.items():
            alpha = strategy_alphas.get(strat, 0.0)
            contribution[strat] = float(weight * alpha)
        return contribution
