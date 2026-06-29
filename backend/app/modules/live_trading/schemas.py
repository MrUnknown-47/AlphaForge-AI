from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class LiveOrderResponse(BaseModel):
    broker_order_id: str
    symbol: str
    qty: float
    side: str
    status: str
    timestamp: datetime

class LiveFillResponse(BaseModel):
    broker_order_id: str
    symbol: str
    price: float
    qty: float
    timestamp: datetime

class LiveTelemetryResponse(BaseModel):
    timestamp: datetime
    symbol: str
    side: str
    quantity: float
    requested_price: float
    executed_price: float
    slippage: float
    commission: float
    latency: float
    broker_order_id: str
    strategy_id: Optional[str] = None

class LivePnlResponse(BaseModel):
    timestamp: datetime
    realized_pnl: float
    unrealized_pnl: float
    daily_pnl: float
    portfolio_pnl: float
    running_equity: float
    buying_power: Optional[float] = None
    cash: Optional[float] = None
    exposure: Optional[float] = None
    margin_utilization: Optional[float] = None
    sector_exposures: Optional[Dict[str, float]] = None
    factor_exposures: Optional[Dict[str, float]] = None

class LiveSlippageResponse(BaseModel):
    symbol: str
    arrival_price: float
    fill_price: float
    slippage_bps: float
    timestamp: datetime

class LiveEventResponse(BaseModel):
    timestamp: datetime
    event_type: str
    message: str

class LiveRiskResponse(BaseModel):
    max_daily_loss: float
    max_position_size: float
    max_exposure: float
    kill_switch_active: bool
    var: Optional[float] = None
    cvar: Optional[float] = None
    drawdown: Optional[float] = None
    beta: Optional[float] = None
    leverage: Optional[float] = None
    liquidity: Optional[float] = None
    concentration: Optional[float] = None
    correlations: Optional[Dict[str, float]] = None
    trigger_state: Optional[str] = None
