from typing import Dict, Any

class RiskCommittee:
    def __init__(self) -> None:
        self.max_volatility_target = 0.20 # 20% max vol target

    def evaluate_risk_limits(self, leverage: float, expected_volatility: float) -> Dict[str, Any]:
        """Risk Committee review of portfolio boundaries."""
        vol_check = expected_volatility <= self.max_volatility_target
        leverage_check = leverage <= 3.0
        approved = vol_check and leverage_check
        return {
            "committee": "Risk Committee",
            "decision": "APPROVED" if approved else "REJECTED (Risk limits exceeded)",
            "details": f"Leverage: {leverage}x, Target Vol: {expected_volatility:.1%}"
        }
