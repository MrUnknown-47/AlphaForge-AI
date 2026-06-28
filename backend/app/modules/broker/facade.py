from typing import Dict, Any, List
from app.modules.broker.service import get_broker

class BrokerFacade:
    def __init__(self) -> None:
        self.broker = get_broker()

    async def get_account(self) -> Dict[str, Any]:
        return await self.broker.get_account()

    async def get_positions(self) -> List[Dict[str, Any]]:
        return await self.broker.get_positions()

    async def place_order(
        self, ticker: str, side: str, qty: float, type: str = "MARKET", price: float = None
    ) -> Dict[str, Any]:
        return await self.broker.place_order(ticker, side, qty, type, price)

    async def close_position(self, ticker: str) -> Dict[str, Any]:
        return await self.broker.close_position(ticker)
