from typing import Dict, Any, List

class HedgingEngine:
    def __init__(self) -> None:
        pass

    def calculate_delta_hedge_trades(self, portfolio_delta: float, underlying_symbol: str) -> Dict[str, Any]:
        """Calculates exact underlying share offset to achieve delta neutral target state."""
        # Share delta = 1.0. To offset +150 delta we must sell 150 shares.
        offset_qty = -portfolio_delta
        action = "SELL" if offset_qty < 0 else "BUY"
        return {
            "underlying_symbol": underlying_symbol,
            "target_hedge_shares": abs(offset_qty),
            "action": action,
            "hedging_method": "Delta Neutral Offset"
        }

    def generate_protective_collar(self, spot: float, symbol: str) -> Dict[str, Any]:
        """Calculates pricing strikes for a protective collar: long stock + long out-of-the-money put + short out-of-the-money call."""
        put_strike = spot * 0.95 # 5% OTM protection
        call_strike = spot * 1.05 # 5% OTM income ceiling
        return {
            "symbol": symbol,
            "protective_put_strike": put_strike,
            "covered_call_strike": call_strike,
            "hedging_method": "Zero-Cost Protective Collar Overlay"
        }
