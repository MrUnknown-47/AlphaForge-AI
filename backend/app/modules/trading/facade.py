import uuid
from app.modules.trading.service import TradingService
from app.modules.trading.schemas import OrderResponse, PositionResponse
from app.modules.trading.models import OrderModel

class TradingFacade:
    """
    Unified entry point for outer modules (like hedge fund simulators) to place mock orders.
    """
    def __init__(self, service: TradingService):
        self._service = service

    async def place_order(self, data) -> OrderResponse:
        order: OrderModel = await self._service.submit_order(data)
        return OrderResponse.from_orm(order)

    async def cancel_order(self, order_id: uuid.UUID) -> None:
        await self._service.cancel_order(order_id)