from typing import Dict, Any

class ForexHedgingEngine:
    def __init__(self) -> None:
        pass

    def calculate_hedging_shares(self, foreign_currency_exposure: float, spot_price: float) -> Dict[str, Any]:
        """Calculates spot FX units needed to hedge a foreign asset exposure back to USD reporting currency."""
        # E.g. 1,000,000 EUR asset exposure at 1.08 spot price requires selling 1,000,000 EUR/USD currency units
        return {
            "exposure_in_foreign_currency": foreign_currency_exposure,
            "required_fx_units": -foreign_currency_exposure,
            "hedge_notional_usd": foreign_currency_exposure * spot_price,
            "action": "SELL"
        }
