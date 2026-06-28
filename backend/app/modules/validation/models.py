from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class LivePerformanceMetrics(BaseModel):
    timestamp: str
    daily_pnl: float
    cumulative_pnl: float
    sharpe: float
    sortino: float
    calmar: float
    max_drawdown: float
    hit_ratio: float
    profit_factor: float

class LiveExecutionQuality(BaseModel):
    timestamp: str
    ticker: str
    expected_price: float
    fill_price: float
    slippage: float
    spread_cost: float
    latency_ms: float
    signal_delay_ms: float

class LiveRiskMetrics(BaseModel):
    timestamp: str
    portfolio_exposure: float
    single_position_exposure: float
    sector_exposure: float
    daily_loss: float
    drawdown: float
    var_95: float
    cvar_95: float

class LiveDriftMetrics(BaseModel):
    timestamp: str
    psi_drift: float
    prediction_confidence: float
    feature_distribution_shifts: Dict[str, float]
    rolling_accuracy: float
    directional_hit_ratio: float

class ValidationScorecard(BaseModel):
    paper_days: int
    sharpe: float
    sortino: float
    max_drawdown: float
    hit_ratio: float
    profit_factor: float
    psi: float
    latency_ms: float
    validation_passed: bool
