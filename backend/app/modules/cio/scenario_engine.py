from typing import Dict, Any

class ScenarioEngine:
    def __init__(self) -> None:
        pass

    def simulate_stress_events(self, allocation: Dict[str, float]) -> Dict[str, Any]:
        """Simulates how the optimized allocation behaves under historical macro black swan shocks."""
        scenarios = {
            "2008 Lehman Default Shock": -0.185,
            "2020 COVID Market Meltdown": -0.124,
            "High Inflation Regime (Stagflation)": -0.045,
            "Low Growth Contraction": -0.021
        }
        
        results = {}
        for name, shock in scenarios.items():
            # portfolio return = sum(w * shock)
            portfolio_impact = sum(w * shock for w in allocation.values())
            results[name] = {
                "portfolio_impact_pct": float(portfolio_impact * 100),
                "status": "PASSED" if portfolio_impact > -0.15 else "FAILED (BREACH)"
            }
        return results
