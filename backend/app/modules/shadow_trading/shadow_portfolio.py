from typing import Dict, List, Any

class ShadowPortfolio:
    def __init__(self) -> None:
        self.cash = 100000.0
        self.portfolio_value = 100000.0
        self.buying_power = 100000.0
        self.exposure_pct = 0.0
        self.daily_return = 0.0
        self.realized_pnl = 0.0
        self.unrealized_pnl = 0.0
        self.positions: Dict[str, Dict[str, float]] = {}

    def update_portfolio_state(
        self, cash: float, portfolio_value: float, buying_power: float, positions: List[Dict[str, Any]]
    ) -> None:
        self.cash = cash
        self.portfolio_value = portfolio_value
        self.buying_power = buying_power
        
        # Open positions mapping
        self.positions = {}
        total_pos_val = 0.0
        total_unrealized = 0.0
        for pos in positions:
            ticker = pos["ticker"]
            qty = pos["quantity"]
            entry = pos["entry_price"]
            market_val = pos.get("market_value", qty * entry)
            unrealized = pos.get("unrealized_pnl", 0.0)
            
            self.positions[ticker] = {
                "quantity": qty,
                "entry_price": entry,
                "market_value": market_val,
                "unrealized_pnl": unrealized
            }
            total_pos_val += abs(qty * entry)
            total_unrealized += unrealized

        self.unrealized_pnl = total_unrealized
        self.exposure_pct = total_pos_val / portfolio_value if portfolio_value > 0.0 else 0.0
