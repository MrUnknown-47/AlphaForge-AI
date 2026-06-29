import asyncio
import logging
from datetime import datetime
from app.core.realtime.manager import ws_bus_manager

logger = logging.getLogger("RiskStream")

class RiskStream:
    def __init__(self) -> None:
        self.is_running = False

    async def start(self) -> None:
        self.is_running = True

    async def stop(self) -> None:
        self.is_running = False

    async def broadcast_risk_metrics(self, metrics: dict) -> None:
        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "metrics": metrics
        }
        await ws_bus_manager.broadcast("risk", payload)

risk_stream_instance = RiskStream()
