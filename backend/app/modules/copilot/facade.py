from typing import Dict, Any
from app.modules.copilot.service import CopilotService
from app.modules.copilot.models import (
    CopilotMarketAnalysis,
    CopilotPortfolioAnalysis,
    CopilotTradeExplanation,
    CopilotRegimeAnalysis,
    CopilotResearchReport
)

class CopilotFacade:
    def __init__(self) -> None:
        self.service = CopilotService()

    async def get_market(self) -> CopilotMarketAnalysis:
        return await self.service.get_market_analysis()

    async def get_portfolio(self) -> CopilotPortfolioAnalysis:
        return await self.service.get_portfolio_analysis()

    async def explain_trade(self, ticker: str, signal: str, confidence: float) -> CopilotTradeExplanation:
        return await self.service.get_trade_explanation(ticker, signal, confidence)

    async def get_regime(self) -> CopilotRegimeAnalysis:
        return await self.service.get_regime_analysis()

    async def get_research(self) -> CopilotResearchReport:
        return await self.service.get_research_report()

    def generate_report(self, report_type: str) -> Dict[str, Any]:
        return self.service.generate_metrics_report(report_type)
