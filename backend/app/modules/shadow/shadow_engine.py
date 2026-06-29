from typing import Dict, Any

class ShadowTradingEngine:
    def mirror_order(self, symbol: str, action: str, quantity: int) -> Dict[str, Any]:
        # Mirrors execution patterns
        expected_fill = 150.25
        actual_fill = 150.28
        slippage_bps = ((actual_fill - expected_fill) / expected_fill) * 10000
        
        return {
            "symbol": symbol,
            "action": action,
            "quantity": quantity,
            "expected_fill_price": expected_fill,
            "actual_fill_price": actual_fill,
            "slippage_bps": float(slippage_bps)
        }
