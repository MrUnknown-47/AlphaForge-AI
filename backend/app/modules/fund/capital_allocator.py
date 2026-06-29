import numpy as np
from typing import Dict, Any, List

class CapitalAllocator:
    def __init__(self) -> None:
        pass

    def allocate_capital_to_strategies(self, aum: float, weights: Dict[str, float]) -> Dict[str, float]:
        """Distributes total AUM across strategies based on target weights."""
        allocations = {}
        for strategy, weight in weights.items():
            allocations[strategy] = float(aum * weight)
        return allocations
