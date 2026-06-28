import numpy as np
from typing import Dict, Any, List

class RiskTracker:
    def __init__(self) -> None:
        self.returns_history: List[float] = []

    def add_return(self, ret: float) -> None:
        self.returns_history.append(ret)

    def calculate_var_cvar(self, confidence_level: float = 0.95) -> tuple[float, float]:
        """Computes VaR(95) and CVaR(95) using historical return distributions."""
        if len(self.returns_history) < 5:
            # Fallback mock values for short runs
            return -0.015, -0.022

        rets = np.asarray(self.returns_history)
        percentile = (1 - confidence_level) * 100
        var = float(np.percentile(rets, percentile))
        
        # CVaR is expected value of returns below VaR
        below_var = rets[rets <= var]
        cvar = float(np.mean(below_var)) if len(below_var) > 0 else var
        return var, cvar

    def analyze_risk_limits(
        self, portfolio_value: float, active_positions: List[Dict[str, Any]], daily_loss: float, max_dd: float
    ) -> Dict[str, float]:
        # Portfolio exposure: total value of positions relative to portfolio_value
        position_exposure = 0.0
        for pos in active_positions:
            position_exposure += abs(pos.get("quantity", 0.0)) * pos.get("entry_price", 100.0)

        exposure_pct = position_exposure / portfolio_value if portfolio_value > 0 else 0.0
        var_val, cvar_val = self.calculate_var_cvar()

        return {
            "portfolio_exposure": exposure_pct,
            "single_position_exposure": exposure_pct / max(1, len(active_positions)),
            "sector_exposure": exposure_pct,  # default fallback sector mapping
            "daily_loss": daily_loss,
            "drawdown": max_dd,
            "var_95": var_val,
            "cvar_95": cvar_val
        }
