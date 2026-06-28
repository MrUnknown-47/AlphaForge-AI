import uuid
from datetime import datetime
from pydantic import BaseModel, Field
from decimal import Decimal

class OrderCreate(BaseModel):
    portfolio_id: uuid.UUID
    ticker: str = Field(..., max_length=16)
    side: str = Field(..., pattern="^(BUY|SELL)$")
    type: str = Field(..., pattern="^(MARKET|LIMIT|STOP|STOP_LIMIT)$")
    quantity: Decimal = Field(..., gt=0)
    price: Decimal | None = Field(None, description="Required for non-market orders")

class OrderResponse(BaseModel):
    id: uuid.UUID
    portfolio_id: uuid.UUID
    ticker: str
    side: str
    type: str
    quantity: Decimal
    price: Decimal | None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class ExecutionResponse(BaseModel):
    id: uuid.UUID
    order_id: uuid.UUID
    execution_price: Decimal
    executed_quantity: Decimal
    fee: Decimal
    executed_at: datetime

    class Config:
        from_attributes = True

class PositionResponse(BaseModel):
    id: uuid.UUID
    portfolio_id: uuid.UUID
    ticker: str
    quantity: Decimal
    average_entry_price: Decimal
    last_updated: datetime

    class Config:
        from_attributes = True