from typing import List, Dict, Any
from app.modules.derivatives.options_engine import OptionsEngine

class GreeksMonitor:
    def __init__(self) -> None:
        self.engine = OptionsEngine()

    def aggregate_portfolio_greeks(self, positions: List[Dict[str, Any]], spot_prices: Dict[str, float]) -> Dict[str, float]:
        """Sums up delta, gamma, and vega exposures across options positions."""
        total_delta = 0.0
        total_gamma = 0.0
        total_vega = 0.0

        for pos in positions:
            symbol = pos.get("symbol", "")
            spot = spot_prices.get(symbol, 150.0)
            qty = pos.get("quantity", 0.0)
            strike = pos.get("strike", spot)
            dte = pos.get("dte", 30.0) / 365.0
            o_type = pos.get("o_type", "call")
            
            greeks = self.engine.black_scholes_greeks(spot, strike, dte, rate=0.042, vol=0.25, o_type=o_type)
            # multiply by qty (1 option contract = 100 shares multiplier)
            multiplier = 100.0 if pos.get("is_option", False) else 1.0
            
            total_delta += greeks["delta"] * qty * multiplier
            total_gamma += greeks["gamma"] * qty * multiplier
            total_vega += greeks["vega"] * qty * multiplier

        return {
            "portfolio_delta": total_delta,
            "portfolio_gamma": total_gamma,
            "portfolio_vega": total_vega
        }
