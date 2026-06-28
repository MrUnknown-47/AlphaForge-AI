from datetime import datetime
from pydantic import BaseModel, Field
from decimal import Decimal

class IndicatorCalculateRequest(BaseModel):
    ticker: str = Field(..., max_length=16)
    indicator_name: str = Field(..., description="e.g. RSI, SMA, MACD")
    parameters: dict = Field(default_factory=dict, description="Custom parameters like period")

class IndicatorCalculateResponse(BaseModel):
    ticker: str
    indicator_name: str
    timestamps: list[datetime]
    values: list[float | dict[str, float]]

class IndicatorsCacheResponse(BaseModel):
    time: datetime
    ticker: str
    rsi_14: Decimal | None
    macd_12_26: Decimal | None
    macd_signal_9: Decimal | None
    bollinger_upper: Decimal | None
    bollinger_lower: Decimal | None
    vwap: Decimal | None

    class Config:
        from_attributes = True