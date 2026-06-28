from fastapi import APIRouter, Depends, status
from app.modules.shadow_validation.facade import ShadowValidationFacade

router = APIRouter(prefix="/shadow-validation", tags=["Institutional Shadow Validation Program"])

def get_validation_facade() -> ShadowValidationFacade:
    return ShadowValidationFacade()

@router.post("/cycle", status_code=status.HTTP_200_OK)
async def trigger_validation_cycle(facade: ShadowValidationFacade = Depends(get_validation_facade)):
    """Triggers one operational shadow validation cycle check."""
    return await facade.execute_cycle()

@router.get("/daily", status_code=status.HTTP_200_OK)
async def get_daily_validation(facade: ShadowValidationFacade = Depends(get_validation_facade)):
    """Returns daily realized/unrealized PnLs and holding logs."""
    return facade.get_daily_logs()

@router.get("/weekly", status_code=status.HTTP_200_OK)
async def get_weekly_validation(facade: ShadowValidationFacade = Depends(get_validation_facade)):
    """Returns rolling weekly Sharpe, Sortino, and Calmar metrics."""
    return facade.get_weekly_logs()

@router.get("/monthly", status_code=status.HTTP_200_OK)
async def get_monthly_validation(facade: ShadowValidationFacade = Depends(get_validation_facade)):
    """Returns CAGR, recovery factors, and maximum drawdowns."""
    return facade.get_monthly_logs()

@router.get("/execution", status_code=status.HTTP_200_OK)
async def get_execution_quality(facade: ShadowValidationFacade = Depends(get_validation_facade)):
    """Returns fill latency, rejection rates, and slippages."""
    return facade.get_execution_stats()

@router.get("/capacity", status_code=status.HTTP_200_OK)
async def get_capacity_simulation(facade: ShadowValidationFacade = Depends(get_validation_facade)):
    """Returns simulated capacity decays and market impact stats."""
    return facade.get_capacity_stats()

@router.get("/scorecard", status_code=status.HTTP_200_OK)
async def get_institutional_scorecard(facade: ShadowValidationFacade = Depends(get_validation_facade)):
    """Returns institutional_readiness_scorecard.json fields."""
    return facade.get_scorecard_details()
