from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class RiskVarResponse(BaseModel):
    symbol: str
    var_parametric: float
    var_historical: float
    var_montecarlo: float

class RiskCvarResponse(BaseModel):
    symbol: str
    cvar_95: float
    expected_shortfall: float

class RiskExposureResponse(BaseModel):
    sector_exposure: Dict[str, float]
    asset_exposure: Dict[str, float]
    leverage: float

class StressScenarioResponse(BaseModel):
    scenario_name: str
    portfolio_loss: float
    expected_drawdown: float
    recovery_time_months: int

class RiskLiquidityResponse(BaseModel):
    symbol: str
    bid_ask_spread_pct: float
    market_impact: float
    liquidation_horizon_days: float

class ContagionResponse(BaseModel):
    systemic_risk_score: float
    contagion_matrix: Dict[str, List[float]]

class RiskLimitsResponse(BaseModel):
    max_drawdown_limit: float
    current_drawdown: float
    limit_breached: bool
    action_required: str