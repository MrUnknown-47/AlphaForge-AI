from typing import List, Dict, Any

class MarketSurveillance:
    def check_wash_trading(self, trades: List[Dict[str, Any]]) -> bool:
        # Detect if buyer == seller mock check
        for t in trades:
            if t.get("buyer_id") == t.get("seller_id"):
                return True
        return False

    def check_spoofing(self, orders: List[Dict[str, Any]]) -> bool:
        # Detect if large order is canceled quickly within 1s
        for o in orders:
            if o.get("action") == "CANCEL" and o.get("duration_ms", 1000) < 500:
                return True
        return False
