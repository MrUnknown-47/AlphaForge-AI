from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class ShadowAccount(BaseModel):
    cash: float
    portfolio_value: float
    buying_power: float
    exposure_pct: float
    daily_return: float

class ShadowPosition(BaseModel):
    ticker: str
    quantity: float
    entry_price: float
    current_price: float
    unrealized_pnl: float

class ReconciliationLog(BaseModel):
    timestamp: str
    reconciliation_ok: bool
    cash_diff: float
    position_mismatches: List[str]

class ShadowExecutionMetric(BaseModel):
    timestamp: str
    ticker: str
    expected_price: float
    fill_price: float
    slippage: float
    spread: float
    latency_ms: float
    rejected: bool

class ShadowValidationReport(BaseModel):
    timestamp: str
    cagr: float
    sharpe: float
    sortino: float
    calmar: float
    hit_ratio: float
    profit_factor: float
    max_drawdown: float
    trading_halted: bool
