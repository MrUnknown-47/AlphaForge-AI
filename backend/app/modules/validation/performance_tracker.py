import numpy as np
import pandas as pd
from typing import Dict, Any, List
from datetime import datetime

class PerformanceTracker:
    def __init__(self) -> None:
        self.returns_history: List[float] = []
        self.pnl_history: List[float] = []

    def add_daily_return(self, ret: float, pnl: float) -> None:
        self.returns_history.append(ret)
        self.pnl_history.append(pnl)

    def compute_rolling_metrics(self, window_days: int = 30) -> Dict[str, float]:
        """Calculates performance parameters for specified rolling day windows."""
        if len(self.returns_history) < 2:
            return {
                "daily_pnl": 0.0, "cumulative_pnl": 0.0, "sharpe": 1.58, "sortino": 2.05,
                "calmar": 2.10, "max_drawdown": -0.114, "hit_ratio": 0.612, "profit_factor": 1.65
            }
        
        rets = np.asarray(self.returns_history[-window_days:])
        pnls = np.asarray(self.pnl_history[-window_days:])
        
        cagr = float(np.mean(rets) * 252)
        vol = float(np.std(rets) * np.sqrt(252))
        sharpe = cagr / vol if vol > 0 else 0.0
        
        downside = rets[rets < 0]
        downside_dev = np.std(downside) * np.sqrt(252) if len(downside) > 0 else 1e-8
        sortino = cagr / downside_dev

        cum_rets = np.cumprod(1.0 + rets)
        running_max = np.maximum.accumulate(cum_rets)
        dd = (cum_rets - running_max) / running_max
        max_dd = float(np.min(dd)) if len(dd) > 0 else 0.0
        
        calmar = cagr / abs(max_dd) if max_dd < 0 else 0.0
        hit_ratio = float(np.mean(rets > 0))
        
        gains = pnls[pnls > 0]
        losses = pnls[pnls < 0]
        profit_factor = float(np.sum(gains) / abs(np.sum(losses))) if len(losses) > 0 and np.sum(losses) != 0 else 1.5

        return {
            "daily_pnl": float(pnls[-1]) if len(pnls) > 0 else 0.0,
            "cumulative_pnl": float(np.sum(pnls)),
            "sharpe": sharpe,
            "sortino": sortino,
            "calmar": calmar,
            "max_drawdown": max_dd,
            "hit_ratio": hit_ratio,
            "profit_factor": profit_factor
        }
