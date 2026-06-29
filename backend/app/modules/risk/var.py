import math
from typing import List

def calculate_parametric_var(returns: List[float], confidence: float = 0.95) -> float:
    if len(returns) < 2:
        return 0.0
    mean_ret = sum(returns) / len(returns)
    variance = sum((x - mean_ret) ** 2 for x in returns) / (len(returns) - 1)
    std_dev = math.sqrt(variance)
    
    # 95% standard normal distribution multiplier is 1.645
    return abs(mean_ret - 1.645 * std_dev)

def calculate_historical_var(returns: List[float], confidence: float = 0.95) -> float:
    if not returns:
        return 0.0
    sorted_ret = sorted(returns)
    idx = int(len(sorted_ret) * (1.0 - confidence))
    return abs(sorted_ret[idx])
