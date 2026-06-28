import os
import json
from datetime import datetime
from typing import Dict, Any, List

class WeeklyTracker:
    def __init__(self, output_dir: str = "backend/app/modules/prediction/reports") -> None:
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.weekly_records: List[Dict[str, Any]] = []

    def log_weekly_metrics(
        self, sharpe: float, sortino: float, calmar: float, vol: float, beta: float, psi: float, conf: float
    ) -> Dict[str, Any]:
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "rolling_sharpe": sharpe,
            "rolling_sortino": sortino,
            "rolling_calmar": calmar,
            "rolling_volatility": vol,
            "rolling_beta": beta,
            "psi_drift": psi,
            "prediction_confidence": conf
        }
        self.weekly_records.append(record)

        # Save to weekly_validation.json
        path = os.path.join(self.output_dir, "weekly_validation.json")
        with open(path, "w") as f:
            json.dump(self.weekly_records, f, indent=4)

        return record
