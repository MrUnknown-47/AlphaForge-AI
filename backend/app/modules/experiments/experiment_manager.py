from typing import Dict, Any, List

class ExperimentManager:
    def __init__(self) -> None:
        self.experiments = {
            "exp_optuna_bayesian_mvo": {"hyperparameters": {"n_trials": 100, "sampler": "TPESampler"}, "metrics": {"best_value": 0.88, "sharpe": 2.15}},
            "exp_gbrt_alpha_model": {"hyperparameters": {"n_estimators": 500, "learning_rate": 0.05}, "metrics": {"best_value": 0.84, "sharpe": 1.95}}
        }

    def list_experiments(self) -> Dict[str, Dict[str, Any]]:
        return self.experiments

    def log_trial(self, name: str, params: Dict[str, Any], metrics: Dict[str, Any]) -> None:
        self.experiments[name] = {"hyperparameters": params, "metrics": metrics}
        # Limit to 10 logs max
        if len(self.experiments) > 10:
            self.experiments.pop(list(self.experiments.keys())[0])
