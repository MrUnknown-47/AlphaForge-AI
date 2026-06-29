import logging
from typing import Dict, Set, Any
from fastapi import WebSocket

logger = logging.getLogger("RealtimeWebSocketManager")

class RealtimeWebSocketManager:
    def __init__(self) -> None:
        # channel_name -> set of connections
        self.active_connections: Dict[str, Set[WebSocket]] = {
            "market": set(),
            "portfolio": set(),
            "execution": set(),
            "risk": set(),
            "operations": set()
        }

    async def connect(self, websocket: WebSocket, channel: str) -> None:
        await websocket.accept()
        if channel in self.active_connections:
            self.active_connections[channel].add(websocket)
            logger.info(f"Client connected to realtime channel: {channel}. Total clients: {len(self.active_connections[channel])}")
        else:
            logger.warning(f"Attempted connection to invalid channel: {channel}")

    def disconnect(self, websocket: WebSocket, channel: str) -> None:
        if channel in self.active_connections and websocket in self.active_connections[channel]:
            self.active_connections[channel].remove(websocket)
            logger.info(f"Client disconnected from channel: {channel}. Total clients: {len(self.active_connections[channel])}")

    async def broadcast(self, channel: str, message: Any) -> None:
        if channel not in self.active_connections:
            return
        
        dead_sockets = set()
        for websocket in self.active_connections[channel]:
            try:
                await websocket.send_json(message)
            except Exception as e:
                logger.warning(f"Error broadcasting to client on channel {channel}: {e}")
                dead_sockets.add(websocket)

        for ws in dead_sockets:
            self.disconnect(ws, channel)

# Global singleton
ws_bus_manager = RealtimeWebSocketManager()
