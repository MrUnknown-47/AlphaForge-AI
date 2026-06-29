from typing import Dict, Any

class TrialManager:
    def __init__(self) -> None:
        pass

    def run_trial(self, trial_id: int, config: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "trial_id": trial_id,
            "status": "COMPLETED",
            "metric_value": 0.85
        }
