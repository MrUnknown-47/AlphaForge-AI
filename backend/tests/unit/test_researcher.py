import pytest
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.strategy_researcher import StrategyResearcher

@pytest.mark.asyncio
async def test_researcher_recommendations():
    provider = LLMProvider()
    researcher = StrategyResearcher(provider)
    perf = {"expected_cagr": 0.24, "expected_sharpe": 1.55}
    psi = {"RSI14": 0.08}
    res = await researcher.generate_research_report(perf, psi)
    
    assert len(res.hypotheses) > 0
    assert len(res.feature_recommendations) > 0
    assert len(res.risk_recommendations) > 0
