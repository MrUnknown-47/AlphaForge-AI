import os
import json
from typing import Dict, Any

class ScorecardGenerator:
    def __init__(self, output_dir: str = "backend/app/modules/prediction/reports") -> None:
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_scorecard(
        self, paper_days: int, sharpe: float, sortino: float, max_drawdown: float,
        hit_ratio: float, profit_factor: float, psi: float, latency_ms: float, daily_loss: float
    ) -> Dict[str, Any]:
        """
        Enforces validation fail gates:
        - Sharpe < 1.0 (fails validation)
        - Hit Ratio < 55% (fails validation)
        - Max Drawdown > 20% (fails validation)
        - PSI > 0.25 (fails validation)
        - Daily Loss > 3% (fails validation)
        """
        # Note max_drawdown is negative, e.g. -0.154 is -15.4%
        dd_pct = abs(max_drawdown)
        
        passed = True
        if sharpe < 1.0:
            passed = False
        if hit_ratio < 0.55:
            passed = False
        if dd_pct > 0.20:
            passed = False
        if psi > 0.25:
            passed = False
        if daily_loss > 0.03:
            passed = False

        scorecard = {
            "paper_days": paper_days,
            "sharpe": sharpe,
            "sortino": sortino,
            "max_drawdown": max_drawdown,
            "hit_ratio": hit_ratio,
            "profit_factor": profit_factor,
            "psi": psi,
            "latency_ms": latency_ms,
            "validation_passed": passed
        }

        path = os.path.join(self.output_dir, "validation_scorecard.json")
        with open(path, "w") as f:
            json.dump(scorecard, f, indent=4)

        return scorecard
