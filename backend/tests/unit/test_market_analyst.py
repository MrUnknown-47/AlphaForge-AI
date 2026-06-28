import pytest
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.market_analyst import MarketAnalyst

@pytest.mark.asyncio
async def test_market_analyst_summaries():
    provider = LLMProvider()
    analyst = MarketAnalyst(provider)
    prices = {"AAPL": 182.50}
    res = await analyst.analyze_market(prices, 0.0015)
    
    assert res.regime == "HIGH_VOLATILITY_GROWTH"
    assert res.sentiment == "BULLISH"
    assert res.confidence == 0.82
    assert "Semiconductor" in res.summary
