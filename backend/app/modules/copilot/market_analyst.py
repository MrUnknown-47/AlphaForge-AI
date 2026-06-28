from typing import Dict, Any
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.models import CopilotMarketAnalysis

class MarketAnalyst:
    def __init__(self, provider: LLMProvider) -> None:
        self.provider = provider

    async def analyze_market(self, prices: Dict[str, float], spy_ret: float) -> CopilotMarketAnalysis:
        prompt = f"""
        Analyze current market dynamics:
        - Asset prices: {prices}
        - SPY Return: {spy_ret:.4f}
        
        Evaluate sector rotation, macro events, and sentiment shifts.
        """
        template = {
            "regime": "HIGH_VOLATILITY_GROWTH",
            "sentiment": "BULLISH",
            "confidence": 0.82,
            "summary": "Semiconductor momentum remains strong."
        }
        res = await self.provider.generate_json(prompt, template)
        return CopilotMarketAnalysis(**res)
