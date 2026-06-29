from typing import Dict, Any

class LiquidityRiskEngine:
    def calculate_liquidity_risk(self, symbol: str, quantity: float, daily_volume: float = 1000000.0) -> Dict[str, Any]:
        spread = 0.0005 # 5 bps
        market_impact = 0.001 * ((quantity / daily_volume) ** 0.5) if daily_volume > 0 else 0.0
        liquidation_horizon = (quantity / (daily_volume * 0.1)) if daily_volume > 0 else 1.0
        
        return {
            "symbol": symbol,
            "bid_ask_spread_pct": spread,
            "market_impact": market_impact,
            "liquidation_horizon_days": max(0.1, liquidation_horizon)
        }
