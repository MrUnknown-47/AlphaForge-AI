import asyncio
import logging
from datetime import datetime
from app.core.realtime.manager import ws_bus_manager

logger = logging.getLogger("ExecutionStream")

class ExecutionStream:
    def __init__(self) -> None:
        self.is_running = False

    async def start(self) -> None:
        self.is_running = True

    async def stop(self) -> None:
        self.is_running = False

    async def broadcast_fill(self, fill_data: dict) -> None:
        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "type": "FILL",
            "data": fill_data
        }
        await ws_bus_manager.broadcast("execution", payload)

    async def broadcast_order(self, order_data: dict) -> None:
        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "type": "ORDER",
            "data": order_data
        }
        await ws_bus_manager.broadcast("execution", payload)

execution_stream_instance = ExecutionStream()
