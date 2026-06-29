from typing import Dict, Any

class BrokerSimulator:
    def __init__(self, commission_rate: float = 0.001, slippage_pct: float = 0.0005) -> None:
        self.commission_rate = commission_rate
        self.slippage_pct = slippage_pct

    def execute_order(self, order_type: str, qty: float, price: float, side: str) -> Dict[str, float]:
        # Slippage calculations
        if side.upper() == "BUY":
            fill_price = price * (1.0 + self.slippage_pct)
        else:
            fill_price = price * (1.0 - self.slippage_pct)
        
        commission = fill_price * qty * self.commission_rate
        return {
            "fill_price": fill_price,
            "commission": commission
        }
