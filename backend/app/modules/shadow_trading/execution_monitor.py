import numpy as np
from datetime import datetime
from typing import Dict, Any, List

class ExecutionMonitor:
    def __init__(self) -> None:
        self.logs: List[Dict[str, Any]] = []

    def log_execution(
        self, ticker: str, expected_price: float, fill_price: float, latency_ms: float, rejected: bool = False
    ) -> Dict[str, Any]:
        slippage = (fill_price - expected_price) / expected_price if not rejected else 0.0
        # Spread cost estimate (mocked at 1.5 bps)
        spread = 0.00015
        
        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "ticker": ticker,
            "expected_price": expected_price,
            "fill_price": fill_price,
            "slippage": slippage,
            "spread": spread,
            "latency_ms": latency_ms,
            "rejected": rejected
        }
        self.logs.append(log)
        return log

    def get_summary_stats(self) -> Dict[str, float]:
        if not self.logs:
            return {"average_slippage": 0.0, "median_latency": 15.0, "fill_percentage": 100.0}

        slippages = [log["slippage"] for log in self.logs if not log["rejected"]]
        latencies = [log["latency_ms"] for log in self.logs]
        rejected_count = sum(1 for log in self.logs if log["rejected"])

        avg_slip = sum(slippages) / len(slippages) if slippages else 0.0
        med_lat = float(np.median(latencies))
        fill_pct = ((len(self.logs) - rejected_count) / len(self.logs)) * 100.0

        return {
            "average_slippage": avg_slip,
            "median_latency": med_lat,
            "fill_percentage": fill_pct
        }
