import pytest
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.portfolio_analyst import PortfolioAnalyst

@pytest.mark.asyncio
async def test_portfolio_analyst_diagnostics():
    provider = LLMProvider()
    analyst = PortfolioAnalyst(provider)
    positions = [{"ticker": "TSLA", "quantity": 100}]
    res = await analyst.analyze_portfolio(50000.0, positions)
    
    assert res.portfolio_health == "GOOD"
    assert "TSLA" in res.largest_risk
    assert "Reduce" in res.recommendation
