from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class CopilotMarketAnalysis(BaseModel):
    regime: str
    sentiment: str
    confidence: float
    summary: str

class CopilotTradeExplanation(BaseModel):
    ticker: str
    signal: str
    confidence: float
    top_features: List[str]
    explanation: str

class CopilotPortfolioAnalysis(BaseModel):
    portfolio_health: str
    largest_risk: str
    drawdown_reason: str
    recommendation: str

class CopilotRegimeAnalysis(BaseModel):
    current_regime: str
    volatility_state: str
    systemic_risk: str

class CopilotResearchReport(BaseModel):
    timestamp: str
    hypotheses: List[str]
    feature_recommendations: List[str]
    risk_recommendations: List[str]
