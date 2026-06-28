from typing import List, Dict, Any
from app.modules.derivatives.pricing_engine.black_scholes import delta, gamma, theta, vega, rho

class GreeksService:
    @staticmethod
    def calculate_greeks(
        S: float, K: float, T: float, r: float, sigma: float, option_type: str = "CALL"
    ) -> Dict[str, float]:
        return {
            "delta": delta(S, K, T, r, sigma, option_type),
            "gamma": gamma(S, K, T, r, sigma),
            "theta": theta(S, K, T, r, sigma, option_type),
            "vega": vega(S, K, T, r, sigma),
            "rho": rho(S, K, T, r, sigma, option_type),
        }

    @staticmethod
    def aggregate_portfolio_greeks(positions: List[Dict[str, Any]]) -> Dict[str, float]:
        total_delta = 0.0
        total_gamma = 0.0
        total_theta = 0.0
        total_vega = 0.0
        total_rho = 0.0

        for pos in positions:
            qty = pos.get("quantity", 0.0)
            S = pos.get("underlying_price", 0.0)
            K = pos.get("strike", 0.0)
            T = pos.get("expiry_years", 0.0)
            r = pos.get("risk_free_rate", 0.05)
            sigma = pos.get("implied_volatility", 0.3)
            option_type = pos.get("option_type", "CALL")

            pos_greeks = GreeksService.calculate_greeks(S, K, T, r, sigma, option_type)
            total_delta += pos_greeks["delta"] * qty
            total_gamma += pos_greeks["gamma"] * qty
            total_theta += pos_greeks["theta"] * qty
            total_vega += pos_greeks["vega"] * qty
            total_rho += pos_greeks["rho"] * qty

        return {
            "delta": total_delta,
            "gamma": total_gamma,
            "theta": total_theta,
            "vega": total_vega,
            "rho": total_rho,
        }
class GreeksEngine:
    pass
