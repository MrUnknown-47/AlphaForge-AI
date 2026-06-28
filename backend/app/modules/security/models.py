from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class SecurityStatus(BaseModel):
    trading_enabled: bool
    kill_switch_active: bool
    broker_mode: str
    anomaly_detected: bool

class AnomalyRecord(BaseModel):
    timestamp: str
    type: str
    severity: str
    description: str

class CapitalGuardState(BaseModel):
    max_single_order: float
    max_position: float
    max_daily_loss: float
    max_portfolio_exposure: float
    requires_manual_confirmation: bool

class SecurityScorecard(BaseModel):
    security_ready: bool
    governance_ready: bool
    real_capital_security_ready: bool
    ready_for_real_capital: bool
