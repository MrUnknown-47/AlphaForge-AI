from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class ResearchFactorResponse(BaseModel):
    name: str
    factor_returns: List[float]
    exposures: Dict[str, float]

class FeatureExplorerResponse(BaseModel):
    name: str
    feature_type: str
    importance: float

class StatValidationResponse(BaseModel):
    test_name: str
    statistic: float
    p_value: float
    passed: bool

class RegimeResponse(BaseModel):
    timestamp: datetime
    regime_name: str
    probability: float

class CorrelationResponse(BaseModel):
    symbol_a: str
    symbol_b: str
    pearson: float
    spearman: float

class ClusterResponse(BaseModel):
    cluster_id: int
    members: List[str]

class ExplainabilityResponse(BaseModel):
    feature_name: str
    shap_value: float