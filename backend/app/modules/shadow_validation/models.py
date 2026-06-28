from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class DailyReport(BaseModel):
    timestamp: str
    realized_pnl: float
    unrealized_pnl: float
    trade_count: int
    hit_ratio: float
    avg_holding_time_hours: float
    exposure: float
    slippage_bps: float
    transaction_cost_usd: float

class WeeklyReport(BaseModel):
    timestamp: str
    rolling_sharpe: float
    rolling_sortino: float
    rolling_calmar: float
    rolling_volatility: float
    rolling_beta: float
    psi_drift: float
    prediction_confidence: float

class MonthlyReport(BaseModel):
    timestamp: str
    cagr: float
    annual_volatility: float
    max_drawdown: float
    profit_factor: float
    expectancy: float
    recovery_factor: float
    var_95: float
    cvar_95: float

class ExecutionQualityStats(BaseModel):
    fill_latency_ms: float
    order_rejection_rate_pct: float
    slippage_bps: float
    spread_cost_bps: float
    broker_uptime_pct: float
    websocket_uptime_pct: float

class CapacityMetrics(BaseModel):
    capital_tier: float
    capacity_decay_pct: float
    market_impact_bps: float
    expected_sharpe: float
    expected_cagr: float

class InstitutionalScorecard(BaseModel):
    expected_cagr: float
    expected_sharpe: float
    expected_sortino: float
    expected_max_drawdown: float
    probability_of_ruin: float
    var_95: float
    cvar_95: float
    capacity_limit_usd: float
    confidence_interval: str
    passed: bool
