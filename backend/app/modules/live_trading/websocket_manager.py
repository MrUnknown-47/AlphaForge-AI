import logging
from fastapi import WebSocket
from typing import List, Dict, Set

logger = logging.getLogger("LiveWebsocketManager")

class LiveWebsocketManager:
    def __init__(self) -> None:
        self.active_connections: Dict[str, Set[WebSocket]] = {
            "orders": set(),
            "fills": set(),
            "pnl": set(),
            "telemetry": set(),
            "events": set()
        }

    async def connect(self, websocket: WebSocket, channel: str) -> None:
        await websocket.accept()
        if channel in self.active_connections:
            self.active_connections[channel].add(websocket)
            logger.info(f"Client connected to live WebSocket channel: {channel}")

    def disconnect(self, websocket: WebSocket, channel: str) -> None:
        if channel in self.active_connections:
            self.active_connections[channel].discard(websocket)
            logger.info(f"Client disconnected from live WebSocket channel: {channel}")

    async def broadcast(self, channel: str, message: dict) -> None:
        if channel in self.active_connections:
            import json
            dead_sockets = set()
            for ws in self.active_connections[channel]:
                try:
                    await ws.send_text(json.dumps(message))
                except Exception:
                    dead_sockets.add(ws)
            for ws in dead_sockets:
                self.active_connections[channel].discard(ws)
