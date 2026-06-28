import uuid
from datetime import datetime
from pydantic import BaseModel, Field
from decimal import Decimal

class ModelRegisterRequest(BaseModel):
    model_name: str = Field(..., max_length=255)
    version: str = Field(..., max_length=64)
    hyperparameters: dict | None = None
    storage_path: str | None = Field(None, max_length=1024)

class ModelRegisterResponse(BaseModel):
    id: uuid.UUID
    model_name: str
    version: str
    hyperparameters: dict | None
    storage_path: str | None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class PredictionQuery(BaseModel):
    tickers: list[str]
    horizon: str = Field(..., pattern="^(1d|5d|20d)$")

class PredictionResponse(BaseModel):
    time: datetime
    ticker: str
    horizon: str
    predicted_value: Decimal
    confidence_lower: Decimal
    confidence_upper: Decimal
    created_at: datetime

    class Config:
        from_attributes = True

class MetricResponse(BaseModel):
    id: uuid.UUID
    model_id: uuid.UUID
    metric_name: str
    metric_value: Decimal
    created_at: datetime

    class Config:
        from_attributes = True