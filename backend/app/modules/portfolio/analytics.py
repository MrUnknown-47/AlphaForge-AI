import math
from typing import List

def calculate_volatility(returns: List[float]) -> float:
    if len(returns) < 2:
        return 0.0
    mean = sum(returns) / len(returns)
    variance = sum((x - mean) ** 2 for x in returns) / (len(returns) - 1)
    return math.sqrt(variance) * math.sqrt(252) # Annualized

def calculate_sharpe(returns: List[float], risk_free_rate: float = 0.02) -> float:
    vol = calculate_volatility(returns)
    if vol == 0:
        return 0.0
    mean_return = sum(returns) / len(returns) * 252 # Annualized
    return (mean_return - risk_free_rate) / vol

def calculate_sortino(returns: List[float], risk_free_rate: float = 0.02) -> float:
    if len(returns) < 2:
        return 0.0
    mean_return = sum(returns) / len(returns) * 252
    downside_returns = [x for x in returns if x < 0]
    if len(downside_returns) < 2:
        return 0.0
    downside_variance = sum(x ** 2 for x in downside_returns) / len(returns)
    downside_deviation = math.sqrt(downside_variance) * math.sqrt(252)
    if downside_deviation == 0:
        return 0.0
    return (mean_return - risk_free_rate) / downside_deviation

def calculate_max_drawdown(equity_curve: List[float]) -> float:
    if not equity_curve:
        return 0.0
    peak = equity_curve[0]
    max_dd = 0.0
    for val in equity_curve:
        if val > peak:
            peak = val
        dd = (peak - val) / peak if peak > 0 else 0.0
        if dd > max_dd:
            max_dd = dd
    return max_dd

def calculate_calmar(returns: List[float], equity_curve: List[float], risk_free_rate: float = 0.02) -> float:
    max_dd = calculate_max_drawdown(equity_curve)
    if max_dd == 0:
        return 0.0
    mean_return = sum(returns) / len(returns) * 252
    return (mean_return - risk_free_rate) / max_dd

def calculate_beta(portfolio_returns: List[float], benchmark_returns: List[float]) -> float:
    if len(portfolio_returns) < 2 or len(portfolio_returns) != len(benchmark_returns):
        return 1.0
    p_mean = sum(portfolio_returns) / len(portfolio_returns)
    b_mean = sum(benchmark_returns) / len(benchmark_returns)
    
    covariance = sum((p - p_mean) * (b - b_mean) for p, b in zip(portfolio_returns, benchmark_returns)) / (len(portfolio_returns) - 1)
    b_variance = sum((b - b_mean) ** 2 for b in benchmark_returns) / (len(benchmark_returns) - 1)
    if b_variance == 0:
        return 1.0
    return covariance / b_variance

def calculate_alpha(portfolio_returns: List[float], benchmark_returns: List[float], risk_free_rate: float = 0.02) -> float:
    p_mean_ann = sum(portfolio_returns) / len(portfolio_returns) * 252
    b_mean_ann = sum(benchmark_returns) / len(benchmark_returns) * 252
    beta = calculate_beta(portfolio_returns, benchmark_returns)
    return p_mean_ann - (risk_free_rate + beta * (b_mean_ann - risk_free_rate))

def calculate_tracking_error(portfolio_returns: List[float], benchmark_returns: List[float]) -> float:
    if len(portfolio_returns) < 2 or len(portfolio_returns) != len(benchmark_returns):
        return 0.0
    active_returns = [p - b for p, b in zip(portfolio_returns, benchmark_returns)]
    return calculate_volatility(active_returns)

def calculate_information_ratio(portfolio_returns: List[float], benchmark_returns: List[float]) -> float:
    te = calculate_tracking_error(portfolio_returns, benchmark_returns)
    if te == 0:
        return 0.0
    p_mean_ann = sum(portfolio_returns) / len(portfolio_returns) * 252
    b_mean_ann = sum(benchmark_returns) / len(benchmark_returns) * 252
    return (p_mean_ann - b_mean_ann) / te
