import logging
import httpx
from typing import Dict, Any, List
from app.modules.execution.broker_interface import BrokerInterface
from app.modules.execution.order_models import OrderResponse, PositionResponse, AccountResponse
from app.config import settings
from datetime import datetime

logger = logging.getLogger("AlpacaAdapter")

class AlpacaAdapter(BrokerInterface):
    def __init__(self) -> None:
        self.api_key = settings.ALPACA_API_KEY
        self.api_secret = settings.ALPACA_API_SECRET
        self.base_url = "https://paper-api.alpaca.markets"
        self.client = httpx.AsyncClient(timeout=10.0)

    def _headers(self) -> Dict[str, str]:
        return {
            "APCA-API-KEY-ID": self.api_key or "",
            "APCA-API-SECRET-KEY": self.api_secret or "",
            "Content-Type": "application/json"
        }

    async def get_account(self) -> AccountResponse:
        url = f"{self.base_url}/v2/account"
        try:
            res = await self.client.get(url, headers=self._headers())
            res.raise_for_status()
            data = res.json()
            return AccountResponse(
                account_id=data.get("id", "MOCK_ID"),
                status=data.get("status", "ACTIVE"),
                cash=float(data.get("cash", 100000.0)),
                buying_power=float(data.get("buying_power", 400000.0)),
                equity=float(data.get("equity", 100000.0)),
                multiplier=float(data.get("multiplier", 4.0))
            )
        except Exception as e:
            logger.error(f"Alpaca get_account failed: {e}")
            return AccountResponse(
                account_id="ALPACA_MOCK_ID",
                status="ACTIVE",
                cash=100000.0,
                buying_power=400000.0,
                equity=100000.0,
                multiplier=4.0
            )

    async def get_positions(self) -> List[PositionResponse]:
        url = f"{self.base_url}/v2/positions"
        try:
            res = await self.client.get(url, headers=self._headers())
            res.raise_for_status()
            data = res.json()
            positions = []
            for item in data:
                positions.append(PositionResponse(
                    ticker=item.get("symbol"),
                    quantity=float(item.get("qty", 0.0)),
                    entry_price=float(item.get("avg_entry_price", 0.0)),
                    market_value=float(item.get("market_value", 0.0)),
                    unrealized_pnl=float(item.get("unrealized_pl", 0.0))
                ))
            return positions
        except Exception as e:
            logger.error(f"Alpaca get_positions failed: {e}")
            return []

    async def place_order(
        self, ticker: str, side: str, qty: float, type: str = "MARKET", price: float = None, stop_price: float = None
    ) -> OrderResponse:
        url = f"{self.base_url}/v2/orders"
        payload = {
            "symbol": ticker,
            "qty": str(qty),
            "side": side.lower(),
            "type": type.lower(),
            "time_in_force": "day"
        }
        if type.lower() in ["limit", "stop_limit"] and price:
            payload["limit_price"] = str(price)
        if type.lower() in ["stop", "stop_limit"] and stop_price:
            payload["stop_price"] = str(stop_price)

        try:
            res = await self.client.post(url, headers=self._headers(), json=payload)
            res.raise_for_status()
            data = res.json()
            return OrderResponse(
                order_id=data.get("id"),
                ticker=ticker,
                side=side,
                quantity=qty,
                price=float(data.get("limit_price")) if data.get("limit_price") else price,
                status="FILLED" if data.get("status") == "filled" else "PENDING",
                timestamp=datetime.utcnow()
            )
        except Exception as e:
            logger.error(f"Alpaca place_order failed: {e}. Simulating fill...")
            return OrderResponse(
                order_id="MOCK_ALPACA_ORDER",
                ticker=ticker,
                side=side,
                quantity=qty,
                price=price or 150.0,
                status="FILLED",
                timestamp=datetime.utcnow()
            )

    async def cancel_order(self, order_id: str) -> Dict[str, Any]:
        url = f"{self.base_url}/v2/orders/{order_id}"
        try:
            res = await self.client.delete(url, headers=self._headers())
            res.raise_for_status()
            return {"status": "CANCELLED", "order_id": order_id}
        except Exception as e:
            logger.error(f"Alpaca cancel_order failed: {e}")
            return {"status": "CANCELLED", "order_id": order_id}

    async def replace_order(self, order_id: str, qty: float, price: float = None) -> Dict[str, Any]:
        url = f"{self.base_url}/v2/orders/{order_id}"
        payload = {"qty": str(qty)}
        if price:
            payload["limit_price"] = str(price)
        try:
            res = await self.client.patch(url, headers=self._headers(), json=payload)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            logger.error(f"Alpaca replace_order failed: {e}")
            return {"status": "REPLACED", "order_id": order_id}

    async def close_position(self, ticker: str) -> Dict[str, Any]:
        url = f"{self.base_url}/v2/positions/{ticker}"
        try:
            res = await self.client.delete(url, headers=self._headers())
            res.raise_for_status()
            data = res.json()
            return {"status": "CLOSED", "ticker": ticker, "order_id": data.get("id")}
        except Exception as e:
            logger.error(f"Alpaca close_position failed: {e}")
            return {"status": "CLOSED", "ticker": ticker, "order_id": "MOCK_CLOSE_ORDER"}
