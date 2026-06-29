import uuid
from datetime import datetime
from pydantic import BaseModel, Field
from decimal import Decimal

class PortfolioCreate(BaseModel):
    name: str = Field(..., max_length=255)

class PortfolioResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    name: str
    cash_balance: Decimal
    created_at: datetime

    class Config:
        from_attributes = True

class HoldingResponse(BaseModel):
    id: uuid.UUID
    ticker: str
    quantity: Decimal

    class Config:
        from_attributes = True

class TransactionCreate(BaseModel):
    transaction_type: str = Field(..., pattern="^(DEPOSIT|WITHDRAW)$")
    amount: Decimal = Field(..., gt=0)

class TransactionResponse(BaseModel):
    id: uuid.UUID
    portfolio_id: uuid.UUID
    transaction_type: str
    amount: Decimal
    created_at: datetime

    class Config:
        from_attributes = True

class PortfolioValuationResponse(BaseModel):
    portfolio_id: uuid.UUID
    nav: Decimal
    unrealized_pnl: Decimal
    realized_pnl: Decimal
    timestamp: datetime

class PortfolioMetricsResponse(BaseModel):
    portfolio_id: uuid.UUID
    sharpe_ratio: Decimal | None
    sortino_ratio: Decimal | None
    max_drawdown: Decimal | None
    volatility: Decimal | None
    beta: Decimal | None
    alpha: Decimal | None
    timestamp: datetime

class AccountSyncResponse(BaseModel):
    account_id: str
    equity: float
    cash: float
    buying_power: float
    portfolio_value: float
    maintenance_margin: float

class PositionSyncResponse(BaseModel):
    symbol: str
    quantity: float
    avg_price: float
    market_price: float
    market_value: float
    unrealized_pnl: float
    unrealized_pct: float

class AllocationResponse(BaseModel):
    symbol: str
    weight: float

class ExposureResponse(BaseModel):
    total_exposure: float
    sector_allocations: dict[str, float]
    asset_allocations: dict[str, float]

class RiskResponse(BaseModel):
    var_95: float
    cvar_95: float
    leverage: float
    concentration_index: float

class AttributionResponse(BaseModel):
    realized_pnl: float
    unrealized_pnl: float
    fees: float
    slippage: float
    contributions: dict[str, float]