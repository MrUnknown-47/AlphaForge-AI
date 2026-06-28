from typing import Dict, Any, List
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.models import CopilotPortfolioAnalysis

class PortfolioAnalyst:
    def __init__(self, provider: LLMProvider) -> None:
        self.provider = provider

    async def analyze_portfolio(self, portfolio_value: float, active_positions: List[Dict[str, Any]]) -> CopilotPortfolioAnalysis:
        prompt = f"""
        Analyze current portfolio status:
        - Portfolio value: ${portfolio_value:.2f}
        - Open Positions: {active_positions}
        
        Evaluate portfolio health, largest risk factor concentration, and suggest hedging suggestions.
        """
        template = {
            "portfolio_health": "GOOD",
            "largest_risk": "TSLA concentration",
            "drawdown_reason": "Technology sector weakness",
            "recommendation": "Reduce TSLA exposure"
        }
        res = await self.provider.generate_json(prompt, template)
        return CopilotPortfolioAnalysis(**res)
