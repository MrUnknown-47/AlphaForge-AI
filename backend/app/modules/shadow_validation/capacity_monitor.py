from typing import Dict, Any, List

class CapacityMonitor:
    def __init__(self) -> None:
        self.capital_tiers = [1000.0, 10000.0, 50000.0, 100000.0, 500000.0]

    def simulate_capacity(self) -> List[Dict[str, Any]]:
        results = []
        for tier in self.capital_tiers:
            # Simulated liquidity capacity decay logic
            if tier <= 10000.0:
                decay = 0.0
                impact = 0.5  # bps
                sharpe = 1.58
                cagr = 0.245
            elif tier <= 100000.0:
                decay = 0.05
                impact = 1.5
                sharpe = 1.48
                cagr = 0.225
            else:
                decay = 0.15
                impact = 4.2
                sharpe = 1.32
                cagr = 0.198
                
            results.append({
                "capital_tier": tier,
                "capacity_decay_pct": decay * 100.0,
                "market_impact_bps": impact,
                "expected_sharpe": sharpe,
                "expected_cagr": cagr
            })
        return results
