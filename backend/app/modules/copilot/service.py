from typing import Dict, Any, List
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.market_analyst import MarketAnalyst
from app.modules.copilot.portfolio_analyst import PortfolioAnalyst
from app.modules.copilot.trade_explainer import TradeExplainer
from app.modules.copilot.regime_detector import RegimeDetector
from app.modules.copilot.strategy_researcher import StrategyResearcher
from app.modules.copilot.report_generator import ReportGenerator
from app.modules.copilot.models import (
    CopilotMarketAnalysis,
    CopilotPortfolioAnalysis,
    CopilotTradeExplanation,
    CopilotRegimeAnalysis,
    CopilotResearchReport
)

class CopilotService:
    def __init__(self) -> None:
        self.provider = LLMProvider()
        self.market_analyst = MarketAnalyst(self.provider)
        self.portfolio_analyst = PortfolioAnalyst(self.provider)
        self.trade_explainer = TradeExplainer(self.provider)
        self.regime_detector = RegimeDetector(self.provider)
        self.researcher = StrategyResearcher(self.provider)
        self.reporter = ReportGenerator()

    async def get_market_analysis(self) -> CopilotMarketAnalysis:
        # Mock rolling feeds input parameters
        prices = {"AAPL": 182.50, "MSFT": 420.10, "NVDA": 122.50}
        return await self.market_analyst.analyze_market(prices, 0.0012)

    async def get_portfolio_analysis(self) -> CopilotPortfolioAnalysis:
        active_pos = [{"ticker": "AAPL", "quantity": 50, "entry_price": 180.0}]
        return await self.portfolio_analyst.analyze_portfolio(100000.0, active_pos)

    async def get_trade_explanation(self, ticker: str, signal: str, confidence: float) -> CopilotTradeExplanation:
        shap = [{"feature": "RSI14", "value": 0.28}, {"feature": "Sentiment", "value": 0.22}]
        return await self.trade_explainer.explain_trade(ticker, signal, confidence, shap, "HIGH_VOLATILITY_GROWTH")

    async def get_regime_analysis(self) -> CopilotRegimeAnalysis:
        corrs = {"AAPL-SPY": 0.75, "MSFT-SPY": 0.82}
        return await self.regime_detector.detect_regime(18.5, 0.18, corrs)

    async def get_research_report(self) -> CopilotResearchReport:
        perf = {"expected_cagr": 0.24, "expected_sharpe": 1.55}
        psi = {"RSI14": 0.08, "Sentiment": 0.12}
        return await self.researcher.generate_research_report(perf, psi)

    def generate_metrics_report(self, report_type: str = "daily") -> Dict[str, Any]:
        perf = {"expected_cagr": 0.24, "expected_sharpe": 1.55, "expected_max_drawdown": -0.154, "hit_ratio": 0.605}
        active_pos = [{"ticker": "AAPL", "quantity": 50, "entry_price": 180.0}]
        return self.reporter.generate_report(report_type, perf, active_pos)
