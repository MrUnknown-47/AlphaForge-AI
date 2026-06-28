import os
import json
from datetime import datetime
from typing import Dict, Any, List

class MonthlyTracker:
    def __init__(self, output_dir: str = "backend/app/modules/prediction/reports") -> None:
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.monthly_records: List[Dict[str, Any]] = []

    def log_monthly_metrics(
        self, cagr: float, vol: float, drawdown: float, pf: float, expectancy: float, recovery: float, var: float, cvar: float
    ) -> Dict[str, Any]:
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "cagr": cagr,
            "annual_volatility": vol,
            "max_drawdown": drawdown,
            "profit_factor": pf,
            "expectancy": expectancy,
            "recovery_factor": recovery,
            "var_95": var,
            "cvar_95": cvar
        }
        self.monthly_records.append(record)

        # Save to monthly_validation.json
        path = os.path.join(self.output_dir, "monthly_validation.json")
        with open(path, "w") as f:
            json.dump(self.monthly_records, f, indent=4)

        return record
