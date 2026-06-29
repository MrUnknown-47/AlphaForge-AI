import asyncio
import logging
from datetime import datetime
from app.core.realtime.manager import ws_bus_manager

logger = logging.getLogger("OpsStream")

class OpsStream:
    def __init__(self) -> None:
        self.is_running = False

    async def start(self) -> None:
        self.is_running = True

    async def stop(self) -> None:
        self.is_running = False

    async def broadcast_ops_status(self, status_report: dict) -> None:
        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "status": status_report
        }
        await ws_bus_manager.broadcast("operations", payload)

ops_stream_instance = OpsStream()
