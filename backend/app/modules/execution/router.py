from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict, Any
from app.modules.execution.execution_router import ExecutionRouter
from app.modules.execution.order_models import OrderRequest, OrderResponse, PositionResponse, AccountResponse

router = APIRouter(tags=["execution"])
exec_router = ExecutionRouter()

@router.get("/broker/health")
async def get_health():
    return {"status": "healthy", "broker": "Alpaca" if exec_router.use_alpaca else "Paper"}

@router.get("/broker/account", response_model=AccountResponse)
async def get_account():
    return await exec_router.get_account()

@router.get("/broker/positions", response_model=List[PositionResponse])
async def get_positions():
    return await exec_router.get_positions()

@router.get("/broker/orders")
async def get_orders():
    # Return local paper orders or simulated list
    if exec_router.use_alpaca:
        return []
    return exec_router.paper.orders

@router.post("/execution/order", response_model=OrderResponse)
async def place_order(req: OrderRequest):
    try:
        return await exec_router.route_order(req)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/execution/cancel")
async def cancel_order(order_id: str):
    return {"status": "CANCELLED", "order_id": order_id}

@router.post("/execution/close")
async def close_position(ticker: str):
    return await exec_router.close_position(ticker)
