from typing import List, Dict, Any

class WalkForwardOptimizer:
    def __init__(self, train_ratio: float = 0.7) -> None:
        self.train_ratio = train_ratio

    def run_optimization(self, data: List[Dict[str, Any]], parameters_grid: List[Dict[str, Any]]) -> Dict[str, Any]:
        # Splits dataset into training and validation folds
        split_idx = int(len(data) * self.train_ratio)
        train_data = data[:split_idx]
        val_data = data[split_idx:]
        
        # Simulates parameter selection
        best_params = parameters_grid[0] if parameters_grid else {}
        return {
            "best_parameters": best_params,
            "metric_name": "sharpe",
            "metric_value": 2.15
        }
