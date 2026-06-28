import pytest
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.trade_explainer import TradeExplainer

@pytest.mark.asyncio
async def test_trade_explainer_narrative():
    provider = LLMProvider()
    explainer = TradeExplainer(provider)
    shap = [{"feature": "RSI14"}]
    res = await explainer.explain_trade("NVDA", "BUY", 0.78, shap, "BULL")
    
    assert res.ticker == "NVDA"
    assert res.signal == "BUY"
    assert res.confidence == 0.78
    assert "RSI14" in res.top_features
    assert "aligned" in res.explanation
