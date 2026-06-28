import uuid
from fastapi import APIRouter, Depends, status
from app.modules.trading.facade import TradingFacade
from app.modules.trading.service import TradingService
from app.modules.trading.dependencies import get_trading_facade, get_trading_service
from app.modules.trading.schemas import OrderCreate, OrderResponse

router = APIRouter(prefix="/trading", tags=["Order Book & Trading"])

@router.post("/orders", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def submit_order(
    data: OrderCreate,
    service: TradingService = Depends(get_trading_service)
):
    return await service.submit_order(data)

@router.post("/orders/{order_id}/cancel", status_code=status.HTTP_200_OK)
async def cancel_order(
    order_id: uuid.UUID,
    facade: TradingFacade = Depends(get_trading_facade)
):
    await facade.cancel_order(order_id)
    return {"message": "Cancellation request submitted"}