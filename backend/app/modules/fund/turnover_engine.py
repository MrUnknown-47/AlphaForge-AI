import numpy as np
from typing import Dict, Any

class TurnoverEngine:
    def __init__(self) -> None:
        pass

    def calculate_turnover(self, current_weights: Dict[str, float], target_weights: Dict[str, float]) -> float:
        """Computes portfolio turnover ratio (sum of absolute changes in weights / 2)."""
        all_assets = set(current_weights.keys()).union(set(target_weights.keys()))
        diff_sum = 0.0
        for asset in all_assets:
            curr = current_weights.get(asset, 0.0)
            target = target_weights.get(asset, 0.0)
            diff_sum += abs(curr - target)
            
        return float(diff_sum / 2.0)
