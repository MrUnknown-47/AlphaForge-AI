from typing import Dict, Any, List

class OptionsStrategyService:
    @staticmethod
    def covered_call(S: float, strike: float, premium: float) -> Dict[str, Any]:
        # Buy stock at S, sell call at strike for premium
        max_profit = (strike - S) + premium if strike > S else premium
        max_loss = S - premium
        breakeven = S - premium
        return {
            "strategy": "Covered Call",
            "max_profit": float(max_profit),
            "max_loss": float(max_loss),
            "breakeven": [float(breakeven)],
            "probability_of_profit": 0.65,
            "expected_value": float(max_profit * 0.65 - max_loss * 0.35)
        }

    @staticmethod
    def cash_secured_put(S: float, strike: float, premium: float) -> Dict[str, Any]:
        # Sell put at strike for premium
        max_profit = premium
        max_loss = strike - premium
        breakeven = strike - premium
        return {
            "strategy": "Cash Secured Put",
            "max_profit": float(max_profit),
            "max_loss": float(max_loss),
            "breakeven": [float(breakeven)],
            "probability_of_profit": 0.70,
            "expected_value": float(max_profit * 0.70 - max_loss * 0.30)
        }

    @staticmethod
    def iron_condor(
        S: float, short_put: float, long_put: float, short_call: float, long_call: float, net_premium: float
    ) -> Dict[str, Any]:
        # Sell short_put, buy long_put (wider/lower), sell short_call, buy long_call (wider/higher)
        max_profit = net_premium
        # Loss width
        put_width = short_put - long_put
        call_width = long_call - short_call
        max_loss = max(put_width, call_width) - net_premium
        breakeven_down = short_put - net_premium
        breakeven_up = short_call + net_premium
        return {
            "strategy": "Iron Condor",
            "max_profit": float(max_profit),
            "max_loss": float(max_loss),
            "breakeven": [float(breakeven_down), float(breakeven_up)],
            "probability_of_profit": 0.75,
            "expected_value": float(max_profit * 0.75 - max_loss * 0.25)
        }

    @staticmethod
    def iron_butterfly(
        S: float, short_strike: float, long_put: float, long_call: float, net_premium: float
    ) -> Dict[str, Any]:
        # Iron Condor but short put & call at same short_strike
        max_profit = net_premium
        put_width = short_strike - long_put
        call_width = long_call - short_strike
        max_loss = max(put_width, call_width) - net_premium
        breakeven_down = short_strike - net_premium
        breakeven_up = short_strike + net_premium
        return {
            "strategy": "Iron Butterfly",
            "max_profit": float(max_profit),
            "max_loss": float(max_loss),
            "breakeven": [float(breakeven_down), float(breakeven_up)],
            "probability_of_profit": 0.55,
            "expected_value": float(max_profit * 0.55 - max_loss * 0.45)
        }

    @staticmethod
    def straddle(S: float, strike: float, net_premium: float) -> Dict[str, Any]:
        # Buy call and put at same strike
        max_profit = float("inf")
        max_loss = net_premium
        breakeven_down = strike - net_premium
        breakeven_up = strike + net_premium
        return {
            "strategy": "Straddle",
            "max_profit": max_profit,
            "max_loss": float(max_loss),
            "breakeven": [float(breakeven_down), float(breakeven_up)],
            "probability_of_profit": 0.40,
            "expected_value": float(-net_premium * 0.60 + 50.0 * 0.40) # arbitrary expectation
        }

    @staticmethod
    def strangle(S: float, put_strike: float, call_strike: float, net_premium: float) -> Dict[str, Any]:
        # Buy OTM call & OTM put
        max_profit = float("inf")
        max_loss = net_premium
        breakeven_down = put_strike - net_premium
        breakeven_up = call_strike + net_premium
        return {
            "strategy": "Strangle",
            "max_profit": max_profit,
            "max_loss": float(max_loss),
            "breakeven": [float(breakeven_down), float(breakeven_up)],
            "probability_of_profit": 0.35,
            "expected_value": float(-net_premium * 0.65 + 75.0 * 0.35)
        }

    @staticmethod
    def calendar_spread(S: float, strike: float, net_premium: float) -> Dict[str, Any]:
        # Buy long expiry, sell short expiry call/put
        max_profit = net_premium * 1.5
        max_loss = net_premium
        breakeven = strike
        return {
            "strategy": "Calendar Spread",
            "max_profit": float(max_profit),
            "max_loss": float(max_loss),
            "breakeven": [float(breakeven)],
            "probability_of_profit": 0.60,
            "expected_value": float(max_profit * 0.60 - max_loss * 0.40)
        }

    @staticmethod
    def bull_call_spread(S: float, long_strike: float, short_strike: float, net_premium: float) -> Dict[str, Any]:
        # Buy call at long_strike, sell call at short_strike
        max_profit = (short_strike - long_strike) - net_premium
        max_loss = net_premium
        breakeven = long_strike + net_premium
        return {
            "strategy": "Bull Call Spread",
            "max_profit": float(max_profit),
            "max_loss": float(max_loss),
            "breakeven": [float(breakeven)],
            "probability_of_profit": 0.58,
            "expected_value": float(max_profit * 0.58 - max_loss * 0.42)
        }

    @staticmethod
    def bear_put_spread(S: float, long_strike: float, short_strike: float, net_premium: float) -> Dict[str, Any]:
        # Buy put at long_strike, sell put at short_strike
        max_profit = (long_strike - short_strike) - net_premium
        max_loss = net_premium
        breakeven = long_strike - net_premium
        return {
            "strategy": "Bear Put Spread",
            "max_profit": float(max_profit),
            "max_loss": float(max_loss),
            "breakeven": [float(breakeven)],
            "probability_of_profit": 0.58,
            "expected_value": float(max_profit * 0.58 - max_loss * 0.42)
        }
class StrategiesEngine:
    pass
