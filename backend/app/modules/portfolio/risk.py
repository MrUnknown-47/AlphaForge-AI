import math
from typing import List, Dict, Any

def calculate_var(returns: List[float], confidence: float = 0.95) -> float:
    # Parametric Value at Risk = Mean - Z * Vol
    if not returns:
        return 0.0
    mean = sum(returns) / len(returns)
    variance = sum((x - mean) ** 2 for x in returns) / len(returns) if len(returns) > 0 else 0.0
    vol = math.sqrt(variance)
    z_score = 1.645 if confidence == 0.95 else 2.326
    return -(mean - z_score * vol)

def calculate_cvar(returns: List[float], confidence: float = 0.95) -> float:
    # Conditional VaR (Expected Shortfall) = Average of returns below VaR
    var_val = calculate_var(returns, confidence)
    tail_returns = [x for x in returns if x <= -var_val]
    if not tail_returns:
        return var_val
    return -sum(tail_returns) / len(tail_returns)

def calculate_leverage(equity: float, portfolio_value: float) -> float:
    if equity <= 0:
        return 1.0
    return portfolio_value / equity

def calculate_concentration(positions: List[Dict[str, Any]]) -> float:
    # Herfindahl-Hirschman Index (HHI) concentration weight metric
    total_val = sum(pos["market_value"] for pos in positions)
    if total_val == 0:
        return 0.0
    hhi = sum((pos["market_value"] / total_val) ** 2 for pos in positions)
    return hhi

def calculate_position_risk(ticker: str, weight: float, asset_vol: float) -> float:
    # Position Marginal Risk Contribution = weight * asset volatility
    return weight * asset_vol

def calculate_portfolio_risk(positions: List[Dict[str, Any]], returns: List[float]) -> float:
    # Returns portfolio volatility
    if len(returns) < 2:
        return 0.0
    mean = sum(returns) / len(returns)
    variance = sum((x - mean) ** 2 for x in returns) / (len(returns) - 1)
    return math.sqrt(variance)
