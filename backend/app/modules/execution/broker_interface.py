from abc import ABC, abstractmethod
from typing import Dict, Any, List
from app.modules.execution.order_models import OrderResponse, PositionResponse, AccountResponse

class BrokerInterface(ABC):
    @abstractmethod
    async def get_account(self) -> AccountResponse:
        pass

    @abstractmethod
    async def get_positions(self) -> List[PositionResponse]:
        pass

    @abstractmethod
    async def place_order(
        self, ticker: str, side: str, qty: float, type: str = "MARKET", price: float = None, stop_price: float = None
    ) -> OrderResponse:
        pass

    @abstractmethod
    async def cancel_order(self, order_id: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def replace_order(self, order_id: str, qty: float, price: float = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def close_position(self, ticker: str) -> Dict[str, Any]:
        pass
