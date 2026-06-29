from typing import Dict, Any, List

class ExperimentComparison:
    def __init__(self) -> None:
        pass

    def compare_runs(self, run_a: Dict[str, Any], run_b: Dict[str, Any]) -> Dict[str, Any]:
        """Compares two experiment run configurations and metrics."""
        return {
            "metric_delta": float(run_a.get("metrics", {}).get("best_value", 0.0) - run_b.get("metrics", {}).get("best_value", 0.0)),
            "parameter_diff": {
                "sampler_match": run_a.get("hyperparameters", {}).get("sampler") == run_b.get("hyperparameters", {}).get("sampler")
            }
        }
