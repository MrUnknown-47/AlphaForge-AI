from typing import List, Dict, Any

class LivePnlEngine:
    def __init__(self) -> None:
        self.realized_pnl = 0.0
        self.starting_equity = 100000.0
        self.running_equity = 100000.0

    def update_pnl(self, positions: List[Dict[str, Any]], cash: float) -> Dict[str, float]:
        unrealized = sum(pos["unrealized_pnl"] for pos in positions)
        current_equity = cash + sum(pos["market_value"] for pos in positions)
        self.running_equity = current_equity
        
        daily_pnl = current_equity - self.starting_equity
        portfolio_pnl = daily_pnl + self.realized_pnl
        
        return {
            "realized_pnl": self.realized_pnl,
            "unrealized_pnl": unrealized,
            "daily_pnl": daily_pnl,
            "portfolio_pnl": portfolio_pnl,
            "running_equity": current_equity
        }
