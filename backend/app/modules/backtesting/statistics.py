import math
from typing import List

def calculate_sharpe(returns: List[float], rf: float = 0.0) -> float:
    if len(returns) < 2:
        return 0.0
    mean_ret = sum(returns) / len(returns)
    variance = sum((x - mean_ret) ** 2 for x in returns) / (len(returns) - 1)
    std_dev = math.sqrt(variance)
    if std_dev <= 0:
        return 0.0
    return (mean_ret - rf) / std_dev

def calculate_sortino(returns: List[float], rf: float = 0.0) -> float:
    if len(returns) < 2:
        return 0.0
    mean_ret = sum(returns) / len(returns)
    downside_returns = [x for x in returns if x < 0]
    if len(downside_returns) < 2:
        return 0.0
    downside_var = sum((x - mean_ret) ** 2 for x in downside_returns) / (len(returns) - 1)
    std_dev = math.sqrt(downside_var)
    if std_dev <= 0:
        return 0.0
    return (mean_ret - rf) / std_dev

def calculate_max_drawdown(equity_curve: List[float]) -> float:
    if not equity_curve:
        return 0.0
    peak = equity_curve[0]
    max_dd = 0.0
    for value in equity_curve:
        if value > peak:
            peak = value
        dd = (peak - value) / peak
        if dd > max_dd:
            max_dd = dd
    return max_dd

def calculate_calmar(returns: List[float], equity_curve: List[float]) -> float:
    max_dd = calculate_max_drawdown(equity_curve)
    if max_dd <= 0:
        return 0.0
    total_ret = (equity_curve[-1] - equity_curve[0]) / equity_curve[0] if len(equity_curve) > 1 else 0.0
    return total_ret / max_dd

def calculate_omega(returns: List[float], threshold: float = 0.0) -> float:
    gains = sum(x - threshold for x in returns if x > threshold)
    losses = sum(threshold - x for x in returns if x < threshold)
    if losses <= 0:
        return 0.0
    return gains / losses
