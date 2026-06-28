from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class HealthStatus(BaseModel):
    api_uptime: float
    polygon_connected: bool
    alpaca_connected: bool
    redis_connected: bool
    db_connected: bool
    ws_reconnects: int
    broker_latency_ms: float

class ModelMetrics(BaseModel):
    sharpe: float
    hit_ratio: float
    prediction_confidence: float
    psi_drift: float
    feature_drift: float
    concept_drift: float
    staleness_hours: float
    aborted: bool

class PortfolioState(BaseModel):
    exposure: float
    leverage: float
    var_95: float
    cvar_95: float
    drawdown: float
    sector_concentration: Dict[str, float]
    correlation_concentration: float
    portfolio_beta: float

class AlertMessage(BaseModel):
    timestamp: str
    severity: str
    message: str

class OperationsScorecard(BaseModel):
    uptime_pct: float
    sharpe: float
    hit_ratio: float
    max_drawdown: float
    reconciliation_accuracy: float
    operations_ready: bool
    ninety_day_validation_ready: bool
    ready_for_real_capital: bool
    end_of_engineering_phase: bool
