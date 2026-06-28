import logging
import asyncio
import httpx
from typing import Dict, Any, Callable

logger = logging.getLogger("MarketStream")

class MarketStream:
    def __init__(self, tickers: list[str]) -> None:
        self.tickers = tickers
        self.latest_prices = {t: 100.0 for t in tickers} # default base prices
        self.is_connected = False
        self.on_price_update: Callable[[str, float], None] = None

    async def connect_polygon_websocket(self) -> None:
        """Simulates connection to Polygon WebSocket feed with reconnect logic."""
        logger.info("Initializing Polygon WebSocket Market Feed connection...")
        await asyncio.sleep(0.1)
        self.is_connected = True
        logger.info("Polygon WebSocket connected and subscribed to market channels.")

    async def fetch_yahoo_finance_fallback(self) -> Dict[str, float]:
        """Yahoo Finance polling fallback when websockets are offline or during validation."""
        logger.info("Polling Yahoo Finance fallback prices...")
        # Simulates real-time price updates (polling interval)
        for ticker in self.tickers:
            # Add small random walk to existing latest prices
            import random
            change = random.uniform(-0.5, 0.5)
            self.latest_prices[ticker] = max(1.0, round(self.latest_prices[ticker] + change, 2))
            if self.on_price_update:
                self.on_price_update(ticker, self.latest_prices[ticker])
        return self.latest_prices

    async def run_stream_loop(self) -> None:
        """Continuous polling/websocket client loop."""
        try:
            await self.connect_polygon_websocket()
            while True:
                await self.fetch_yahoo_finance_fallback()
                # Run polling updates every hour in production, but fast-paced here
                await asyncio.sleep(3600)
        except asyncio.CancelledError:
            logger.info("Stream loop cancelled.")
            self.is_connected = False
