from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class CIOAllocationResponse(BaseModel):
    timestamp: datetime
    allocation: Dict[str, float]
    leverage: float
    turnover: float

class CIORegimeResponse(BaseModel):
    timestamp: datetime
    regime: str
    description: str

class CIORiskBudgetResponse(BaseModel):
    timestamp: datetime
    budget: Dict[str, float]

class CIOHedgesResponse(BaseModel):
    timestamp: datetime
    hedges: Dict[str, Any]

class CIOExplanationsResponse(BaseModel):
    timestamp: datetime
    explanations: Dict[str, str]

class CIORecommendationsResponse(BaseModel):
    timestamp: datetime
    recommendations: Dict[str, Any]
