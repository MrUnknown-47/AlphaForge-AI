from datetime import datetime
from typing import Dict, Any, List
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.models import CopilotResearchReport

class StrategyResearcher:
    def __init__(self, provider: LLMProvider) -> None:
        self.provider = provider

    async def generate_research_report(
        self, performance_summary: Dict[str, Any], psi_drifts: Dict[str, float]
    ) -> CopilotResearchReport:
        prompt = f"""
        Analyze system model performance parameters:
        - performance_summary: {performance_summary}
        - psi_drifts: {psi_drifts}
        
        Identify model confidence drops and generate research hypotheses and feature recommendations.
        """
        template = {
            "timestamp": datetime.utcnow().isoformat(),
            "hypotheses": [
                "Feature drift in PE ratios is causing degradation in QQQ performance.",
                "Short signal bounds should be expanded under Bear regimes."
            ],
            "feature_recommendations": ["Rolling 10d beta decay", "Sentiment Momentum"],
            "risk_recommendations": ["Reduce max exposure to 40% when VIX > 25"]
        }
        res = await self.provider.generate_json(prompt, template)
        return CopilotResearchReport(**res)
