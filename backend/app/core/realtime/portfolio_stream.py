import asyncio
import logging
from datetime import datetime
from app.core.realtime.manager import ws_bus_manager
from app.modules.execution.alpaca_adapter import AlpacaAdapter

logger = logging.getLogger("PortfolioStream")

class PortfolioStream:
    def __init__(self) -> None:
        self.adapter = AlpacaAdapter()
        self.is_running = False

    async def start(self) -> None:
        self.is_running = True
        asyncio.create_task(self._run_loop())

    async def stop(self) -> None:
        self.is_running = False

    async def _run_loop(self) -> None:
        while self.is_running:
            try:
                acc = await self.adapter.get_account()
                payload = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "equity": acc.equity,
                    "cash": acc.cash,
                    "buying_power": acc.buying_power,
                    "unrealized_pnl": 0.0,  # Computed by live portfolio updates
                    "realized_pnl": 0.0
                }
                await ws_bus_manager.broadcast("portfolio", payload)
                await asyncio.sleep(2.0)
            except Exception as e:
                logger.error(f"Error in PortfolioStream loop: {e}")
                await asyncio.sleep(5.0)

portfolio_stream_instance = PortfolioStream()
