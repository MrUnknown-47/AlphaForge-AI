import uuid
from datetime import datetime
from pydantic import BaseModel

class OptionContractResponse(BaseModel):
    id: uuid.UUID
    symbol: str
    underlying: str
    expiry: datetime
    strike: float
    option_type: str
    bid: float
    ask: float
    last: float
    volume: int
    open_interest: int
    implied_volatility: float
    delta: float
    gamma: float
    theta: float
    vega: float
    rho: float
    timestamp: datetime

    class Config:
        from_attributes = True

class FuturesContractResponse(BaseModel):
    id: uuid.UUID
    symbol: str
    root: str
    expiry: datetime
    contract_size: int
    settlement: float
    volume: int
    open_interest: int
    margin_requirement: float
    timestamp: datetime

    class Config:
        from_attributes = True

class GreeksResponse(BaseModel):
    delta: float
    gamma: float
    theta: float
    vega: float
    rho: float

class StrategyRiskResponse(BaseModel):
    strategy: str
    max_profit: float
    max_loss: float
    breakeven: list[float]
    probability_of_profit: float
    expected_value: float

class VolatilitySurfaceResponse(BaseModel):
    strikes: list[float]
    expiries_days: list[int]
    surface: list[list[float]]
