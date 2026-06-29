from typing import Dict, Any

class InvestmentCommittee:
    def __init__(self) -> None:
        pass

    def evaluate_allocations(self, target_weights: Dict[str, float]) -> Dict[str, Any]:
        """Investment Committee approval check for strategy allocations."""
        # E.g. approve if weights sum to exactly 1.0 (or under leverage limits)
        total_w = sum(target_weights.values())
        approved = 0.95 <= total_w <= 3.0
        return {
            "committee": "Investment Committee",
            "decision": "APPROVED" if approved else "REJECTED (Weights Out of Bounds)",
            "details": f"Total strategy allocation sum: {total_w:.2%}"
        }
