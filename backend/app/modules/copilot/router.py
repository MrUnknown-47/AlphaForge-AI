from fastapi import APIRouter, Depends, Query, status
from app.modules.copilot.facade import CopilotFacade
from app.modules.copilot.models import (
    CopilotMarketAnalysis,
    CopilotPortfolioAnalysis,
    CopilotTradeExplanation,
    CopilotRegimeAnalysis,
    CopilotResearchReport
)

router = APIRouter(prefix="/copilot", tags=["AI Copilot Analyst Module"])

def get_copilot_facade() -> CopilotFacade:
    return CopilotFacade()

@router.get("/market", response_model=CopilotMarketAnalysis, status_code=status.HTTP_200_OK)
async def get_market_analysis(facade: CopilotFacade = Depends(get_copilot_facade)):
    """Returns AI market regime, macro rotation, and sentiment shift summaries."""
    return await facade.get_market()

@router.get("/portfolio", response_model=CopilotPortfolioAnalysis, status_code=status.HTTP_200_OK)
async def get_portfolio_analysis(facade: CopilotFacade = Depends(get_copilot_facade)):
    """Returns portfolio health diagnostic, risk exposures, and concentration recommendations."""
    return await facade.get_portfolio()

@router.get("/trades/{id}", response_model=CopilotTradeExplanation, status_code=status.HTTP_200_OK)
async def get_trade_explanation(
    id: str,
    ticker: str = Query("AAPL", description="Asset symbol"),
    signal: str = Query("BUY", description="Executed signal BUY/SELL"),
    confidence: float = Query(0.85, description="Prediction confidence"),
    facade: CopilotFacade = Depends(get_copilot_facade)
):
    """Explains a specific model trade entry using SHAP rankings and predictions confidence."""
    return await facade.explain_trade(ticker, signal, confidence)

@router.get("/regime", response_model=CopilotRegimeAnalysis, status_code=status.HTTP_200_OK)
async def get_market_regime(facade: CopilotFacade = Depends(get_copilot_facade)):
    """Detects systemic market regimes and volatility levels from market volatility parameters."""
    return await facade.get_regime()

@router.get("/research", response_model=CopilotResearchReport, status_code=status.HTTP_200_OK)
async def get_research_report(facade: CopilotFacade = Depends(get_copilot_facade)):
    """Formulates strategy research hypotheses, feature expansions, and risk optimization adjustments."""
    return await facade.get_research()

@router.get("/report", status_code=status.HTTP_200_OK)
async def generate_metrics_report(
    report_type: str = Query("daily", description="Daily, weekly, or monthly report"),
    facade: CopilotFacade = Depends(get_copilot_facade)
):
    """Generates and exports daily/weekly/monthly strategy performance reports."""
    return facade.generate_report(report_type)
