from typing import Dict, Any, List

class ExecutionPlanner:
    def __init__(self) -> None:
        pass

    def generate_rebalance_orders(self, current_weights: Dict[str, float], target_weights: Dict[str, float], aum: float) -> List[Dict[str, Any]]:
        """Generates buy/sell actions based on weights delta and total AUM."""
        orders = []
        all_assets = set(current_weights.keys()).union(set(target_weights.keys()))
        
        for asset in all_assets:
            curr = current_weights.get(asset, 0.0)
            target = target_weights.get(asset, 0.0)
            delta = target - curr
            
            if abs(delta) > 0.01:
                action = "BUY" if delta > 0 else "SELL"
                orders.append({
                    "symbol": asset,
                    "action": action,
                    "target_weight_delta": float(delta),
                    "order_value_usd": float(abs(delta) * aum)
                })
        return orders
