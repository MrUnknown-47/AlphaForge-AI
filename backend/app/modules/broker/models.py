from pydantic import BaseModel
from typing import Optional, List

class BrokerAccount(BaseModel):
    account_id: str
    cash: float
    portfolio_value: float
    buying_power: float
    currency: str = "USD"

class BrokerPosition(BaseModel):
    ticker: str
    quantity: float
    entry_price: float
    market_value: float
    unrealized_pnl: float

class BrokerOrder(BaseModel):
    order_id: str
    ticker: str
    side: str  # BUY / SELL
    type: str  # MARKET / LIMIT
    quantity: float
    price: Optional[float] = None
    status: str  # PENDING / FILLED / REJECTED
