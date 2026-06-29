from typing import Dict, Any, List

class AllocationCommittee:
    def __init__(self) -> None:
        pass

    def vote(self, tickers: List[str], regime: str) -> Dict[str, Any]:
        """Runs the voting round among macro, technical, risk, and derivatives agents."""
        decisions = {}
        for ticker in tickers:
            # Simulated voting matrix
            if regime == "BEAR":
                vote_action = "REDUCE"
                confidence = 0.88
            elif regime == "CRISIS":
                vote_action = "HEDGE"
                confidence = 0.95
            else:
                vote_action = "BUY"
                confidence = 0.82
            
            decisions[ticker] = {
                "recommendation": vote_action,
                "confidence": confidence,
                "votes": {
                    "Macro Agent": "BUY" if regime == "BULL" else "REDUCE",
                    "Technical Agent": "BUY" if regime == "BULL" else "HOLD",
                    "Risk Agent": "HOLD" if regime == "BULL" else "HEDGE",
                    "Derivatives Agent": "HOLD" if regime == "BULL" else "HEDGE"
                }
            }
        return decisions
