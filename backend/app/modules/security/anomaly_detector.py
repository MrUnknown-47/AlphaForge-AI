from datetime import datetime
from typing import Dict, Any, List

class AnomalyDetector:
    def __init__(self) -> None:
        self.anomaly_logs: List[Dict[str, Any]] = []

    def inspect_traffic(
        self, order_frequency: float, exposure_pct: float, latency_ms: float, login_failures: int
    ) -> List[Dict[str, Any]]:
        """Alerts on abnormal order frequency or unusual latency spikes."""
        anomalies = []
        
        if order_frequency > 10.0:
            anomalies.append({
                "timestamp": datetime.utcnow().isoformat(),
                "type": "ORDER_FREQUENCY_SPIKE",
                "severity": "CRITICAL",
                "description": f"Abnormal trade frequency detected: {order_frequency} orders/sec"
            })
            
        if latency_ms > 500.0:
            anomalies.append({
                "timestamp": datetime.utcnow().isoformat(),
                "type": "LATENCY_SPIKE",
                "severity": "WARNING",
                "description": f"Latency spike detected: {latency_ms} ms"
            })

        if login_failures > 5:
            anomalies.append({
                "timestamp": datetime.utcnow().isoformat(),
                "type": "LOGIN_ABUSE_ATTEMPT",
                "severity": "CRITICAL",
                "description": f"Consecutive login failures: {login_failures}"
            })

        self.anomaly_logs.extend(anomalies)
        return anomalies
