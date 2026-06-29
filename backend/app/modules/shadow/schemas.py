from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class ShadowStatusResponse(BaseModel):
    shadow_run_id: str
    status: str # ACTIVE, INACTIVE
    uptime_days: int

class ShadowPerformanceResponse(BaseModel):
    sharpe: float
    sortino: float
    max_drawdown: float
    win_rate: float
    profit_factor: float

class ShadowReconcileResponse(BaseModel):
    status: str # MATCH, WARNING, BREAK
    internal_cash: float
    broker_cash: float
    cash_variance: float
    reconciled_at: datetime

class ShadowExecutionQualityResponse(BaseModel):
    symbol: str
    implementation_shortfall_bps: float
    vwap_slippage_bps: float
    latency_ms: float
    fill_ratio: float

class ShadowCertifyResponse(BaseModel):
    certified: bool
    shadow_period_days_elapsed: int
    zero_critical_failures: bool
    reconciliation_breaks_count: int
    readiness_score: float
