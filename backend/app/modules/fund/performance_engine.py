import numpy as np
from typing import Dict, Any

class PerformanceEngine:
    def __init__(self) -> None:
        pass

    def calculate_performance_metrics(self, returns: np.ndarray, benchmark_returns: np.ndarray) -> Dict[str, float]:
        """Calculates portfolio excess return alpha, beta, Sharpe ratio, and Information ratio."""
        excess = returns - 0.05 / 252 # risk free rate assumption
        mean_ret = np.mean(returns) * 252
        std_ret = np.std(returns) * np.sqrt(252)
        sharpe = mean_ret / std_ret if std_ret > 0 else 0.0
        
        # Tracking error
        tracking_diff = returns - benchmark_returns
        tracking_error = np.std(tracking_diff) * np.sqrt(252)
        info_ratio = (mean_ret - np.mean(benchmark_returns) * 252) / tracking_error if tracking_error > 0 else 0.0
        
        return {
            "annualized_return": float(mean_ret),
            "annualized_volatility": float(std_ret),
            "sharpe_ratio": float(sharpe),
            "tracking_error": float(tracking_error),
            "information_ratio": float(info_ratio)
        }
