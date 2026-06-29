import random
from typing import List, Dict, Any

class MonteCarloSimulator:
    def __init__(self, num_simulations: int = 1000) -> None:
        self.num_simulations = num_simulations

    def run_simulation(self, historical_returns: List[float], initial_equity: float = 100000.0, periods: int = 252) -> Dict[str, Any]:
        if not historical_returns:
            historical_returns = [0.0005, -0.0002, 0.001, -0.0008, 0.0012] # Fallback path
            
        paths = []
        ruin_count = 0
        final_values = []
        
        for _ in range(self.num_simulations):
            equity = initial_equity
            path = [equity]
            for _ in range(periods):
                change = random.choice(historical_returns)
                equity *= (1.0 + change)
                path.append(equity)
                if equity < initial_equity * 0.5: # 50% drawdown threshold count as ruin
                    ruin_count += 1
                    break
            paths.append(path)
            final_values.append(equity)
            
        ruin_probability = ruin_count / self.num_simulations
        final_values.sort()
        
        # 95% Confidence Band intervals
        p5 = final_values[int(self.num_simulations * 0.05)]
        p95 = final_values[int(self.num_simulations * 0.95)]
        
        return {
            "ruin_probability": ruin_probability,
            "confidence_bands_95": [p5, p95]
        }
