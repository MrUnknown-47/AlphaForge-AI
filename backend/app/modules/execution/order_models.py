from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class OrderRequest(BaseModel):
    ticker: str
    side: str
    quantity: float
    order_type: str = "MARKET"
    price: Optional[float] = None

class OrderResponse(BaseModel):
    order_id: str
    ticker: str
    side: str
    quantity: float
    price: Optional[float] = None
    status: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class PositionResponse(BaseModel):
    ticker: str
    quantity: float
    entry_price: float
    market_value: float
    unrealized_pnl: float

class AccountResponse(BaseModel):
    account_id: str
    status: str
    cash: float
    buying_power: float
    equity: float
    multiplier: float
