from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class MlModelResponse(BaseModel):
    id: str
    name: str
    version: str
    status: str

class PredictionResponse(BaseModel):
    symbol: str
    predicted_return: float
    confidence: float
    uncertainty_score: float

class MetricResponse(BaseModel):
    metric_name: str
    value: float

class RegimePredResponse(BaseModel):
    regime: str
    probability: float

class DriftResponse(BaseModel):
    feature_name: str
    psi: float
    drift_detected: bool

class ExplainResponse(BaseModel):
    feature_name: str
    importance: float
