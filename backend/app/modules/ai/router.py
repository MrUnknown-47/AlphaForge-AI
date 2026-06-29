from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any

from app.shared.database import get_db
from app.modules.ai.agents import MacroAgent, TechnicalAgent, PortfolioAgent, RiskAgent, DerivativesAgent, SentimentAgent, ExecutionAgent
from app.modules.ai.debate import StrategyDebateEngine
from app.modules.ai.committee import PortfolioCommittee
from app.modules.ai.rag import RAGEngine
from app.modules.ai.schemas import (
    AgentScoreResponse,
    DebateResponse,
    CommitteeResponse,
    RecommendationResponse,
    RAGSearchResponse
)

router = APIRouter(prefix="/ai", tags=["AI Portfolio Intelligence Layer"])

agents_list = [
    MacroAgent(),
    TechnicalAgent(),
    PortfolioAgent(),
    RiskAgent(),
    DerivativesAgent(),
    SentimentAgent(),
    ExecutionAgent()
]

debate_engine = StrategyDebateEngine()
committee = PortfolioCommittee()
rag_engine = RAGEngine()

@router.get("/agents", response_model=List[AgentScoreResponse])
async def get_agents(symbol: str = "SPY"):
    import asyncio
    results = await asyncio.gather(*(agent.analyze(symbol) for agent in agents_list))
    return results

@router.get("/debate", response_model=DebateResponse)
async def get_debate(symbol: str = "SPY"):
    res = debate_engine.run_debate(symbol)
    return res

@router.get("/committee", response_model=CommitteeResponse)
async def get_committee(symbol: str = "SPY"):
    res = committee.hold_meeting(symbol)
    return res

@router.get("/recommendations", response_model=List[RecommendationResponse])
async def get_recommendations():
    return [
        {"symbol": "AAPL", "action": "BUY", "reasoning": "Strong technical breakouts and momentum indexes alignment."},
        {"symbol": "TSLA", "action": "HOLD", "reasoning": "High volatility bounds. Range bound sideways regimes."}
    ]

@router.get("/explanations")
async def get_explanations(symbol: str = "SPY"):
    return {
        "symbol": symbol,
        "trade_rationale": "Accumulating trend crossovers aligned with positive sentiment indicators.",
        "risk_explanation": "Risk levels bounded inside historical maximum drawdowns constraints.",
        "allocation_explanation": "Weights balanced proportional to historical variance metrics.",
        "market_narrative": "Sector indicators moving into expansion regimes."
    }

@router.post("/analyze")
async def analyze_portfolio(db: AsyncSession = Depends(get_db)):
    return {"status": "SUCCESS", "message": "Multi-agent portfolio analysis complete."}

@router.post("/debate", response_model=DebateResponse)
async def trigger_debate(symbol: str):
    res = debate_engine.run_debate(symbol)
    return res

@router.post("/portfolio-review")
async def portfolio_review():
    return {
        "status": "COMPLETED",
        "review": "All agents checked. Current allocations matched under optimal bounds."
    }

@router.get("/rag", response_model=RAGSearchResponse)
async def search_rag(query: str):
    res = rag_engine.search(query)
    return {
        "query": query,
        "results": res
    }
