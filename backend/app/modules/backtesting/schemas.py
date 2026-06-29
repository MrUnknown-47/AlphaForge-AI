from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class BacktestRunRequest(BaseModel):
    strategy_name: str
    symbol: str
    start_date: str
    end_date: str
    parameters: Dict[str, Any] = {}

class BacktestRunResponse(BaseModel):
    run_id: str
    strategy_name: str
    status: str
    started_at: datetime

class BacktestMetricsResponse(BaseModel):
    sharpe: float
    sortino: float
    calmar: float
    max_drawdown: float
    win_rate: float
    profit_factor: float

class BacktestTradeResponse(BaseModel):
    symbol: str
    price: float
    qty: float
    side: str
    timestamp: datetime

class OptimizationResponse(BaseModel):
    best_parameters: Dict[str, Any]
    metric_name: str
    metric_value: float

class MonteCarloResponse(BaseModel):
    simulation_paths: int
    ruin_probability: float
    confidence_bands_95: List[float]