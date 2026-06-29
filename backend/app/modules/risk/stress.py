from typing import Dict, Any

class StressTestingEngine:
    def __init__(self) -> None:
        self.scenarios = {
            "Black Monday 1987": {"loss": 0.226, "drawdown": 0.30, "recovery": 18},
            "Dot-com Crash 2000": {"loss": 0.49, "drawdown": 0.50, "recovery": 48},
            "Financial Crisis 2008": {"loss": 0.56, "drawdown": 0.57, "recovery": 60},
            "COVID Crash 2020": {"loss": 0.339, "drawdown": 0.34, "recovery": 5},
            "Inflation Shock": {"loss": 0.12, "drawdown": 0.15, "recovery": 12},
            "Rate Hike Shock": {"loss": 0.08, "drawdown": 0.10, "recovery": 8}
        }

    def evaluate_scenario(self, scenario_name: str, portfolio_value: float) -> Dict[str, Any]:
        scen = self.scenarios.get(scenario_name, {"loss": 0.05, "drawdown": 0.05, "recovery": 6})
        return {
            "scenario_name": scenario_name,
            "portfolio_loss": float(portfolio_value * scen["loss"]),
            "expected_drawdown": scen["drawdown"],
            "recovery_time_months": scen["recovery"]
        }
