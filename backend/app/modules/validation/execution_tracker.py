from typing import Dict, Any, List

class ExecutionTracker:
    def __init__(self) -> None:
        self.execution_logs: List[Dict[str, Any]] = []

    def log_execution(
        self, ticker: str, expected_price: float, fill_price: float, latency_ms: float, delay_ms: float
    ) -> Dict[str, Any]:
        slippage = (fill_price - expected_price) / expected_price
        # Spread cost estimate (mocked at 1.5 bps)
        spread_cost = 0.00015
        
        log = {
            "ticker": ticker,
            "expected_price": expected_price,
            "fill_price": fill_price,
            "slippage": slippage,
            "spread_cost": spread_cost,
            "latency_ms": latency_ms,
            "signal_delay_ms": delay_ms
        }
        self.execution_logs.append(log)
        return log

    def get_average_metrics(self) -> Dict[str, float]:
        if not self.execution_logs:
            return {"avg_slippage": 0.0, "avg_latency_ms": 15.0, "avg_delay_ms": 45.0}

        slippages = [log["slippage"] for log in self.execution_logs]
        latencies = [log["latency_ms"] for log in self.execution_logs]
        delays = [log["signal_delay_ms"] for log in self.execution_logs]

        return {
            "avg_slippage": sum(slippages) / len(slippages),
            "avg_latency_ms": sum(latencies) / len(latencies),
            "avg_delay_ms": sum(delays) / len(delays)
        }
