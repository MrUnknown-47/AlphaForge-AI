import logging
from typing import Dict, Any
from app.modules.broker.service import get_broker
from app.config import settings

logger = logging.getLogger("AlpacaExecutor")

class AlpacaExecutor:
    def __init__(self) -> None:
        # Enforce Alpaca PAPER trading ONLY
        settings.BROKER = "ALPACA"
        self.broker = get_broker()

    async def execute_trade(
        self, ticker: str, side: str, qty: float, type: str = "MARKET", price: float = None
    ) -> Dict[str, Any]:
        """Executes a BUY/SELL order (market or limit) on Alpaca Paper Trading."""
        logger.info(f"Routing order to Alpaca Paper: {side} {qty} {ticker} (Type: {type})")
        res = await self.broker.place_order(ticker, side, qty, type, price)
        return res
