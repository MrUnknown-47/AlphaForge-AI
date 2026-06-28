import numpy as np
from typing import Dict, Any, List

class RiskService:
    @staticmethod
    def calculate_var_cvar(returns: List[float], confidence_level: float = 0.95) -> Dict[str, float]:
        if not returns:
            return {"var": 0.0, "cvar": 0.0}
        arr = np.array(returns)
        var = np.percentile(arr, (1.0 - confidence_level) * 100)
        # CVaR is mean of returns below VaR
        cvar = arr[arr <= var].mean() if len(arr[arr <= var]) > 0 else var
        return {
            "var": float(-var),
            "cvar": float(-cvar)
        }

    @staticmethod
    def calculate_greeks_exposure(positions: List[Dict[str, Any]]) -> Dict[str, float]:
        total_delta_dollar = 0.0
        total_gamma_dollar = 0.0
        total_vega_dollar = 0.0

        for pos in positions:
            qty = pos.get("quantity", 0)
            S = pos.get("underlying_price", 0.0)
            
            delta = pos.get("delta", 0.0)
            gamma = pos.get("gamma", 0.0)
            vega = pos.get("vega", 0.0)

            # Dollar Greeks: Delta = Delta * Qty * S, Gamma = 0.5 * Gamma * Qty * S^2 * 1%
            total_delta_dollar += delta * qty * S
            total_gamma_dollar += 0.5 * gamma * qty * (S ** 2) * 0.01
            total_vega_dollar += vega * qty * 100.0

        return {
            "delta_exposure": total_delta_dollar,
            "gamma_exposure": total_gamma_dollar,
            "vega_exposure": total_vega_dollar
        }

    @staticmethod
    def perform_stress_tests(positions: List[Dict[str, Any]]) -> Dict[str, float]:
        # Test extreme movements: -30% stock crash, +50% volatility spike
        scenarios = {
            "black_monday_crash": {"shock_S": -0.30, "shock_vol": 0.50},
            "volatility_crush": {"shock_S": 0.05, "shock_vol": -0.40},
            "interest_rate_hike": {"shock_S": -0.02, "shock_vol": 0.05}
        }
        
        results = {}
        for name, params in scenarios.items():
            scenario_loss = 0.0
            shock_S = params["shock_S"]
            shock_vol = params["shock_vol"]
            
            for pos in positions:
                qty = pos.get("quantity", 0)
                S = pos.get("underlying_price", 0.0)
                delta = pos.get("delta", 0.0)
                gamma = pos.get("gamma", 0.0)
                vega = pos.get("vega", 0.0)
                
                dS = S * shock_S
                # Options PnL Taylor expansion approximation: delta * dS + 0.5 * gamma * dS^2 + vega * dVol
                pnl = qty * (delta * dS + 0.5 * gamma * dS**2 + vega * shock_vol * 100.0)
                scenario_loss += pnl
                
            results[name] = float(-scenario_loss) # return positive loss

        return results
class RiskEngine:
    pass
