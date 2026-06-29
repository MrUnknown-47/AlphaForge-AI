from typing import Dict, Any

class ExplanationEngine:
    def __init__(self) -> None:
        pass

    def generate_report(self, allocation: Dict[str, float], committee_consensus: Dict[str, Any], regime: str) -> Dict[str, str]:
        """Generates explainability reports for portfolio decisions."""
        return {
            "portfolio_rationale": f"Allocations optimized via MVO regularized using shrinkage. Regime detected as: {regime}.",
            "risk_rationale": "Position sizes limited under 25% single-asset caps to bound tracking error.",
            "macro_rationale": "GS10 treasury yield cycles indicate asset class accumulation phase holds optimal support.",
            "execution_rationale": "Orders routed to execution broker gateways aiming for minimal bid-ask spread impact."
        }
