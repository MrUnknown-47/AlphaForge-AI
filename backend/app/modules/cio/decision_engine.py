import numpy as np
from typing import Dict, Any

class DecisionEngine:
    def __init__(self) -> None:
        pass

    def apply_tactical_adjustments(self, raw_weights: Dict[str, float], committee_consensus: Dict[str, Any], regime: str) -> Dict[str, float]:
        """Applies tactical scaling/modifiers to weights based on consensus recommendation and regime."""
        adjusted = {}
        for ticker, weight in raw_weights.items():
            consensus = committee_consensus.get(ticker, {})
            rec = consensus.get("recommendation", "BUY")
            
            # Modifier logic
            modifier = 1.0
            if rec == "REDUCE":
                modifier = 0.5
            elif rec == "HEDGE":
                modifier = 0.8
            elif rec == "EXIT":
                modifier = 0.0
            elif rec == "BUY" and regime == "BULL":
                modifier = 1.2
                
            adjusted[ticker] = float(np.clip(weight * modifier, 0.0, 1.0))
            
        # Re-normalize to 1.0 sum if not leveraged
        sum_w = sum(adjusted.values())
        if sum_w > 0:
            adjusted = {k: v / sum_w for k, v in adjusted.items()}
        return adjusted
