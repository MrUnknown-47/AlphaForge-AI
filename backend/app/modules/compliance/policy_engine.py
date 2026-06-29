from typing import Dict, Any

class CompliancePolicyEngine:
    def evaluate_order(self, symbol: str, quantity: int) -> Dict[str, Any]:
        # Pre-trade policy checks
        if symbol == "XYZ":
            return {"allowed": False, "policy_action": "REJECT", "reason": "Asset XYZ is on restricted list."}
        elif quantity > 10000:
            return {"allowed": False, "policy_action": "ESCALATE", "reason": "Order size exceeds PM limit."}
        elif quantity > 5000:
            return {"allowed": True, "policy_action": "WARN", "reason": "Position concentration warning."}
        else:
            return {"allowed": True, "policy_action": "ALLOW", "reason": "Order fits parameters."}
