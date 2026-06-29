import pytest
from app.modules.ai.agents import MacroAgent, TechnicalAgent, PortfolioAgent, RiskAgent
from app.modules.ai.debate import StrategyDebateEngine
from app.modules.ai.committee import PortfolioCommittee
from app.modules.ai.rag import RAGEngine

@pytest.mark.asyncio
async def test_ai_agents():
    agent = MacroAgent()
    res = await agent.analyze("AAPL")
    
    assert res["name"] == "Macro Agent"
    assert res["score"] == 0.82
    assert res["confidence"] == 0.90
    assert "GS10" in res["reasoning"]

@pytest.mark.asyncio
async def test_ai_debate():
    debate = StrategyDebateEngine()
    res = debate.run_debate("AAPL")
    
    assert res["consensus_score"] == 0.68
    assert "bull_thesis" in res
    assert "bear_thesis" in res

@pytest.mark.asyncio
async def test_ai_committee():
    comm = PortfolioCommittee()
    res = comm.hold_meeting("AAPL")
    
    assert res["decision"] == "BUY"
    assert "Chairman" in res["votes"]

@pytest.mark.asyncio
async def test_ai_rag():
    rag = RAGEngine()
    res = rag.search("allocations")
    
    assert len(res) > 0
    assert "content" in res[0]
