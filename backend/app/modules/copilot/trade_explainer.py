from typing import Dict, Any, List
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.models import CopilotTradeExplanation

class TradeExplainer:
    def __init__(self, provider: LLMProvider) -> None:
        self.provider = provider

    async def explain_trade(
        self, ticker: str, signal: str, confidence: float, shap_rankings: List[Dict[str, Any]], regime: str
    ) -> CopilotTradeExplanation:
        prompt = f"""
        Explain the model signal logic:
        - Ticker: {ticker}
        - Signal: {signal}
        - Model Confidence: {confidence:.4f}
        - SHAP feature importance rankings: {shap_rankings}
        - Current Market Regime: {regime}
        
        Provide a concise research narrative on why the trade was generated.
        """
        template = {
            "ticker": ticker,
            "signal": signal,
            "confidence": confidence,
            "top_features": [item.get("feature", "RSI14") for item in shap_rankings[:4]] if shap_rankings else ["RSI14"],
            "explanation": "Momentum and sentiment aligned."
        }
        res = await self.provider.generate_json(prompt, template)
        return CopilotTradeExplanation(**res)
