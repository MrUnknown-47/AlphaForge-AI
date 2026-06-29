import numpy as np
from typing import Dict, Any, List

class StrategyWeightEngine:
    def __init__(self) -> None:
        pass

    def compute_strategy_weights(self, ranked_strategies: List[Dict[str, Any]]) -> Dict[str, float]:
        """Calculates optimal strategy weight distribution (simple top-k allocation)."""
        num_strats = len(ranked_strategies)
        if num_strats == 0:
            return {}
        
        # Assign weights proportionally to positive alphas
        raw_weights = {}
        total_alpha = 0.0
        for entry in ranked_strategies:
            strat = entry["strategy"]
            alpha = max(0.0, entry["expected_alpha"])
            raw_weights[strat] = alpha
            total_alpha += alpha
            
        if total_alpha > 0:
            return {k: v / total_alpha for k, v in raw_weights.items()}
        else:
            return {entry["strategy"]: 1.0 / num_strats for entry in ranked_strategies}
