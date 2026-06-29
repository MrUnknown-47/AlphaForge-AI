from typing import List, Dict, Any

def calculate_market_value(positions: List[Dict[str, Any]]) -> float:
    return sum(pos["quantity"] * pos["market_price"] for pos in positions)

def calculate_unrealized_pnl(positions: List[Dict[str, Any]]) -> float:
    return sum(pos["unrealized_pnl"] for pos in positions)

def calculate_daily_return(current_equity: float, previous_equity: float) -> float:
    if previous_equity <= 0:
        return 0.0
    return (current_equity - previous_equity) / previous_equity
