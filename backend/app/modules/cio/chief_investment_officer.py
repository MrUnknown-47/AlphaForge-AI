import logging
from typing import Dict, Any, List
from app.modules.portfolio_optimization.allocation import CapitalAllocationEngine
from app.modules.cio.allocation_committee import AllocationCommittee
from app.modules.cio.decision_engine import DecisionEngine
from app.modules.cio.scenario_engine import ScenarioEngine
from app.modules.cio.explanation_engine import ExplanationEngine

logger = logging.getLogger("ChiefInvestmentOfficer")

class ChiefInvestmentOfficer:
    def __init__(self) -> None:
        self.allocation_engine = CapitalAllocationEngine()
        self.committee = AllocationCommittee()
        self.decision_engine = DecisionEngine()
        self.scenario_engine = ScenarioEngine()
        self.explanation_engine = ExplanationEngine()

    async def run_allocation_cycle(self, tickers: List[str], returns_data: Any, regime: str = "BULL") -> Dict[str, Any]:
        """Runs the entire CIO office allocation workflow."""
        # 1. Optimize weights
        raw_alloc = self.allocation_engine.generate_allocations(tickers, returns_data, method="MVO")
        
        # 2. Gather committee votes
        committee_consensus = self.committee.vote(tickers, regime)
        
        # 3. Decision Engine adjustments (overrides allocation based on consensus and regime)
        final_alloc = self.decision_engine.apply_tactical_adjustments(raw_alloc, committee_consensus, regime)
        
        # 4. Stress tests via Scenario engine
        stress_test = self.scenario_engine.simulate_stress_events(final_alloc)
        
        # 5. Build explainability report
        explanation = self.explanation_engine.generate_report(final_alloc, committee_consensus, regime)

        return {
            "regime": regime,
            "optimized_allocation": final_alloc,
            "committee_decisions": committee_consensus,
            "stress_tests": stress_test,
            "explanations": explanation
        }
