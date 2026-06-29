from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class AgentScoreResponse(BaseModel):
    name: str
    score: float
    confidence: float
    reasoning: str
    recommendation: str

class DebateResponse(BaseModel):
    symbol: str
    bull_thesis: str
    bear_thesis: str
    consensus_score: float
    confidence_score: float
    portfolio_action: str

class CommitteeResponse(BaseModel):
    decision: str
    votes: Dict[str, str]
    rationale: str

class RecommendationResponse(BaseModel):
    symbol: str
    action: str
    reasoning: str

class RAGSearchResponse(BaseModel):
    query: str
    results: List[Dict[str, Any]]
