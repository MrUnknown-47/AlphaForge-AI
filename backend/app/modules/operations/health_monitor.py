import logging
from typing import Dict, Any
from app.modules.operations.uptime_tracker import UptimeTracker

logger = logging.getLogger("HealthMonitor")

class HealthMonitor:
    def __init__(self, tracker: UptimeTracker) -> None:
        self.tracker = tracker
        self.broker_latency_ms = 45.0

    def check_health(self) -> Dict[str, Any]:
        uptime = self.tracker.calculate_uptime()
        
        # SRE Alert triggers
        if uptime < 99.0:
            logger.warning(f"CRITICAL ALERT: API uptime fell below 99% threshold! Uptime: {uptime:.2f}%")
        if self.broker_latency_ms > 500.0:
            logger.warning(f"CRITICAL ALERT: Broker execution latency exceeded 500ms limit! Latency: {self.broker_latency_ms}ms")

        return {
            "api_uptime": uptime,
            "polygon_connected": True,
            "alpaca_connected": True,
            "redis_connected": True,
            "db_connected": True,
            "ws_reconnects": self.tracker.ws_reconnects,
            "broker_latency_ms": self.broker_latency_ms
        }
