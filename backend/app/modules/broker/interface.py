from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BrokerInterface(ABC):
    @abstractmethod
    async def get_account(self) -> Dict[str, Any]:
        """Returns account metadata: cash, portfolio value, buying power."""
        pass

    @abstractmethod
    async def get_positions(self) -> List[Dict[str, Any]]:
        """Returns a list of open positions."""
        pass

    @abstractmethod
    async def place_order(
        self, ticker: str, side: str, qty: float, type: str = "MARKET", price: float = None
    ) -> Dict[str, Any]:
        """Places a trading order (buy/sell)."""
        pass

    @abstractmethod
    async def close_position(self, ticker: str) -> Dict[str, Any]:
        """Liquidates/closes open position for a ticker."""
        pass
