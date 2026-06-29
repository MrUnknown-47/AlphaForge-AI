import math
from typing import Dict, Any

class OptionsEngine:
    def __init__(self) -> None:
        pass

    def black_scholes_greeks(
        self, spot: float, strike: float, time_to_expiry: float, rate: float, vol: float, o_type: str = "call"
    ) -> Dict[str, float]:
        """Calculates Black-Scholes price and greeks: Delta, Gamma, Vega."""
        if time_to_expiry <= 0 or vol <= 0:
            return {"price": max(0.0, spot - strike) if o_type == "call" else max(0.0, strike - spot), "delta": 1.0 if o_type == "call" else -1.0, "gamma": 0.0, "vega": 0.0}

        d1 = (math.log(spot / strike) + (rate + 0.5 * vol ** 2) * time_to_expiry) / (vol * math.sqrt(time_to_expiry))
        d2 = d1 - vol * math.sqrt(time_to_expiry)

        # Standard cumulative normal distribution helper
        def norm_cdf(x):
            return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

        def norm_pdf(x):
            return math.exp(-0.5 * x ** 2) / math.sqrt(2 * math.pi)

        price = 0.0
        delta = 0.0
        gamma = 0.0
        vega = 0.0

        if o_type.lower() == "call":
            price = spot * norm_cdf(d1) - strike * math.exp(-rate * time_to_expiry) * norm_cdf(d2)
            delta = norm_cdf(d1)
        else:
            price = strike * math.exp(-rate * time_to_expiry) * norm_cdf(-d2) - spot * norm_cdf(-d1)
            delta = norm_cdf(d1) - 1.0

        gamma = norm_pdf(d1) / (spot * vol * math.sqrt(time_to_expiry))
        vega = spot * math.sqrt(time_to_expiry) * norm_pdf(d1)

        return {
            "price": price,
            "delta": delta,
            "gamma": gamma,
            "vega": vega
        }
