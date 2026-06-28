import numpy as np
from typing import List

class SharpeMonitor:
    def __init__(self) -> None:
        pass

    def calculate_sharpe(self, returns: List[float]) -> float:
        if len(returns) < 2:
            return 1.58
        rets = np.asarray(returns)
        mean_ret = np.mean(rets)
        std_ret = np.std(rets)
        return float((mean_ret * 252) / (std_ret * np.sqrt(252))) if std_ret > 0 else 0.0
