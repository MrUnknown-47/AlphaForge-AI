from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class LivePrediction(BaseModel):
    timestamp: str
    ticker: str
    xgboost_pred: float
    lstm_pred: float
    ensemble_pred: float

class LiveSignal(BaseModel):
    timestamp: str
    ticker: str
    action: str  # BUY / SELL / HOLD
    confidence: float

class LivePosition(BaseModel):
    ticker: str
    quantity: float
    entry_price: float
    current_price: float
    unrealized_pnl: float

class LiveAlert(BaseModel):
    timestamp: str
    alert_type: str  # DRAWDOWN / POSITION_LIMIT / LOSS_LIMIT / PSI_DRIFT
    message: str

class LiveMetrics(BaseModel):
    timestamp: str
    portfolio_value: float
    drawdown: float
    daily_pnl: float
    hit_ratio: float
