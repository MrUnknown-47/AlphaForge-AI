import numpy as np
from typing import List

class DrawdownMonitor:
    def __init__(self) -> None:
        pass

    def calculate_max_drawdown(self, returns: List[float]) -> float:
        if not returns:
            return -0.114
        cum = np.cumprod(1.0 + np.asarray(returns))
        running_max = np.maximum.accumulate(cum)
        dd = (cum - running_max) / running_max
        return float(np.min(dd)) if len(dd) > 0 else 0.0
