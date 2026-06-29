import asyncio
import json
import logging
from app.core.realtime.manager import ws_bus_manager
from app.services.market_data.aggregator import MarketDataAggregator

logger = logging.getLogger("MarketStream")

class MarketStream:
    def __init__(self) -> None:
        self.aggregator = MarketDataAggregator()
        self.is_running = False

    async def start(self) -> None:
        self.is_running = True
        asyncio.create_task(self._run_loop())

    async def stop(self) -> None:
        self.is_running = False

    async def _run_loop(self) -> None:
        while self.is_running:
            try:
                # Poll aggregator for live prices of key assets
                for symbol in ["AAPL", "NVDA", "MSFT", "GOOGL"]:
                    price = await self.aggregator.get_live_price(symbol)
                    payload = {
                        "symbol": symbol,
                        "price": float(price),
                        "timestamp": datetime.utcnow().isoformat() if hasattr(datetime, "utcnow") else ""
                    }
                    # We can use datetime locally or mock timestamp
                    from datetime import datetime
                    payload["timestamp"] = datetime.utcnow().isoformat()
                    await ws_bus_manager.broadcast("market", payload)
                await asyncio.sleep(1.0)
            except Exception as e:
                logger.error(f"Error in MarketStream loop: {e}")
                await asyncio.sleep(5.0)

market_stream_instance = MarketStream()
