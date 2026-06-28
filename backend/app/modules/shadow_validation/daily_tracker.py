import os
import json
from datetime import datetime
from typing import Dict, Any, List

class DailyTracker:
    def __init__(self, output_dir: str = "backend/app/modules/prediction/reports") -> None:
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.daily_records: List[Dict[str, Any]] = []

    def log_daily_metrics(
        self, realized: float, unrealized: float, trades: int, hit_ratio: float,
        holding_time: float, exposure: float, slippage: float, tx_cost: float
    ) -> Dict[str, Any]:
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "realized_pnl": realized,
            "unrealized_pnl": unrealized,
            "trade_count": trades,
            "hit_ratio": hit_ratio,
            "avg_holding_time_hours": holding_time,
            "exposure": exposure,
            "slippage_bps": slippage * 10000.0,
            "transaction_cost_usd": tx_cost
        }
        self.daily_records.append(record)
        
        # Save to daily_validation.json
        path = os.path.join(self.output_dir, "daily_validation.json")
        with open(path, "w") as f:
            json.dump(self.daily_records, f, indent=4)
            
        return record
