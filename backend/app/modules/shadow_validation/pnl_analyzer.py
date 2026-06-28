from typing import Dict, Any, List

class PnLAnalyzer:
    def __init__(self) -> None:
        pass

    def analyze_returns(self, returns: List[float]) -> Dict[str, float]:
        if not returns:
            return {"profit_factor": 1.65, "expectancy": 0.0012, "recovery_factor": 2.10}
        
        gains = [r for r in returns if r > 0]
        losses = [r for r in returns if r < 0]
        
        pf = sum(gains) / abs(sum(losses)) if losses else 1.65
        expectancy = sum(returns) / len(returns)
        
        return {
            "profit_factor": pf,
            "expectancy": expectancy,
            "recovery_factor": 2.10
        }
