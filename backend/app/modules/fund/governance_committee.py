from typing import Dict, Any

class GovernanceCommittee:
    def __init__(self) -> None:
        pass

    def check_regulatory_compliance(self, wash_trading_alerts: int, spoofing_alerts: int) -> Dict[str, Any]:
        """Governance Committee regulatory audit check."""
        approved = (wash_trading_alerts == 0) and (spoofing_alerts == 0)
        return {
            "committee": "Governance Committee",
            "decision": "APPROVED" if approved else "REJECTED (Surveillance Alerts Flagged)",
            "details": f"Wash: {wash_trading_alerts}, Spoof: {spoofing_alerts}"
        }
