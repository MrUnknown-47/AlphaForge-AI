from fastapi import APIRouter, HTTPException, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
from datetime import datetime
import uuid

from app.shared.database import get_db
from app.modules.live_trading.execution_monitor import ExecutionMonitor
from app.modules.live_trading.risk_monitor import LiveRiskMonitor
from app.modules.live_trading.pnl_engine import LivePnlEngine
from app.modules.live_trading.websocket_manager import LiveWebsocketManager
from app.modules.live_trading.telemetry import calculate_slippage_bps, calculate_implementation_shortfall, calculate_market_impact
from app.modules.live_trading.schemas import (
    LiveOrderResponse,
    LiveFillResponse,
    LiveTelemetryResponse,
    LivePnlResponse,
    LiveSlippageResponse,
    LiveEventResponse,
    LiveRiskResponse
)
from app.modules.live_trading.db_models import (
    ExecutionOrderModel,
    ExecutionFillModel,
    ExecutionPositionModel,
    ExecutionTelemetryModel,
    ExecutionPnlModel,
    ExecutionSlippageModel,
    ExecutionEventModel,
    ExecutionSessionModel
)

router = APIRouter(prefix="/live", tags=["Live Execution Monitoring"])

monitor = ExecutionMonitor()
risk_monitor = LiveRiskMonitor()
pnl_engine = LivePnlEngine()
ws_manager = LiveWebsocketManager()

@router.get("/orders", response_model=List[LiveOrderResponse])
async def get_orders():
    orders = await monitor.get_live_orders()
    return orders

@router.get("/fills", response_model=List[LiveFillResponse])
async def get_fills(db: AsyncSession = Depends(get_db)):
    # Returns last filled transactions
    return [
        {
            "broker_order_id": "MOCK_FILL_1",
            "symbol": "AAPL",
            "price": 150.05,
            "qty": 1.0,
            "timestamp": datetime.utcnow()
        }
    ]

@router.get("/positions", response_model=List[Dict[str, Any]])
async def get_positions():
    return await monitor.get_live_positions()

@router.get("/pnl", response_model=LivePnlResponse)
async def get_pnl():
    acc = await monitor.router.get_account()
    positions = await monitor.router.get_positions()
    
    total_market_val = sum(p.market_value for p in positions)
    unrealized = sum(p.unrealized_pnl for p in positions)
    
    # Simple calculations
    exposure = total_market_val / acc.equity if acc.equity > 0 else 0.0
    margin_utilization = max(0.0, (acc.equity - acc.cash) / acc.equity) if acc.equity > 0 else 0.0
    
    # Mock sector/factor exposures mapping
    sector_exposures = {"Technology": 0.65, "Healthcare": 0.15, "Financials": 0.20}
    factor_exposures = {"Value": 0.45, "Growth": 0.85, "Momentum": 1.25}

    return {
        "timestamp": datetime.utcnow(),
        "realized_pnl": 0.0,
        "unrealized_pnl": unrealized,
        "daily_pnl": total_market_val * 0.015, # Simulated intraday change
        "portfolio_pnl": unrealized,
        "running_equity": acc.equity,
        "buying_power": acc.buying_power,
        "cash": acc.cash,
        "exposure": exposure,
        "margin_utilization": margin_utilization,
        "sector_exposures": sector_exposures,
        "factor_exposures": factor_exposures
    }

@router.get("/telemetry", response_model=List[LiveTelemetryResponse])
async def get_telemetry():
    return [
        {
            "timestamp": datetime.utcnow(),
            "symbol": "AAPL",
            "side": "BUY",
            "quantity": 1.0,
            "requested_price": 150.0,
            "executed_price": 150.05,
            "slippage": 0.05,
            "commission": 0.0,
            "latency": 45.2,
            "broker_order_id": "MOCK_ORDER_1"
        }
    ]

@router.get("/slippage", response_model=List[LiveSlippageResponse])
async def get_slippage():
    slippage_bps = calculate_slippage_bps(150.0, 150.05, "BUY")
    return [
        {
            "symbol": "AAPL",
            "arrival_price": 150.0,
            "fill_price": 150.05,
            "slippage_bps": slippage_bps,
            "timestamp": datetime.utcnow()
        }
    ]

@router.get("/events", response_model=List[LiveEventResponse])
async def get_events():
    return [
        {
            "timestamp": datetime.utcnow(),
            "event_type": "ORDER_FILLED",
            "message": "Simulated order filled for AAPL quantity 1"
        }
    ]

@router.get("/risk", response_model=LiveRiskResponse)
async def get_risk():
    acc = await monitor.router.get_account()
    positions = await monitor.router.get_positions()
    
    total_market_val = sum(p.market_value for p in positions)
    leverage = total_market_val / acc.equity if acc.equity > 0 else 0.0
    
    # Concentration: largest position pct
    max_pos_val = max([p.market_value for p in positions]) if positions else 0.0
    concentration = max_pos_val / total_market_val if total_market_val > 0 else 0.0
    
    # Mock VaR and CVaR (95% 1-day)
    var_val = total_market_val * 0.024
    cvar_val = total_market_val * 0.038
    
    # Determine trigger state: WARNING, REDUCE, LIQUIDATE, KILL_SWITCH
    trigger_state = "NORMAL"
    if risk_monitor.kill_switch_active:
        trigger_state = "KILL_SWITCH"
    elif leverage > 2.0:
        trigger_state = "LIQUIDATE"
    elif leverage > 1.5:
        trigger_state = "REDUCE"
    elif leverage > 1.0:
        trigger_state = "WARNING"

    return {
        "max_daily_loss": risk_monitor.max_daily_loss,
        "max_position_size": risk_monitor.max_position_pct,
        "max_exposure": risk_monitor.max_portfolio_exposure,
        "kill_switch_active": risk_monitor.kill_switch_active,
        "var": var_val,
        "cvar": cvar_val,
        "drawdown": 0.015, # Simulated drawdown
        "beta": 1.15,
        "leverage": leverage,
        "liquidity": 0.98,
        "concentration": concentration,
        "correlations": {"AAPL_NVDA": 0.62, "AAPL_SPY": 0.88, "NVDA_SPY": 0.72},
        "trigger_state": trigger_state
    }

@router.post("/kill-switch")
async def toggle_kill_switch(active: bool):
    risk_monitor.set_kill_switch(active)
    return {"status": "SUCCESS", "kill_switch_active": risk_monitor.kill_switch_active}

@router.post("/flatten")
async def emergency_flatten(db: AsyncSession = Depends(get_db)):
    await risk_monitor.emergency_flatten(db)
    return {"status": "SUCCESS", "message": "Flatten order sent."}

# WebSockets Endpoint Channels
@router.websocket("/ws/live/orders")
async def ws_live_orders(websocket: WebSocket):
    await ws_manager.connect(websocket, "orders")
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket, "orders")

@router.websocket("/ws/live/fills")
async def ws_live_fills(websocket: WebSocket):
    await ws_manager.connect(websocket, "fills")
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket, "fills")

@router.websocket("/ws/live/pnl")
async def ws_live_pnl(websocket: WebSocket):
    await ws_manager.connect(websocket, "pnl")
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket, "pnl")

@router.websocket("/ws/live/telemetry")
async def ws_live_telemetry(websocket: WebSocket):
    await ws_manager.connect(websocket, "telemetry")
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket, "telemetry")

@router.websocket("/ws/live/events")
async def ws_live_events(websocket: WebSocket):
    await ws_manager.connect(websocket, "events")
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket, "events")
