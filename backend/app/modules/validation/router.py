from fastapi import APIRouter, Depends, status
from app.modules.validation.facade import ValidationFacade

router = APIRouter(prefix="/validation", tags=["Live Paper Validation Framework"])

def get_validation_facade() -> ValidationFacade:
    return ValidationFacade()

@router.post("/cycle", status_code=status.HTTP_200_OK)
async def trigger_validation_cycle(facade: ValidationFacade = Depends(get_validation_facade)):
    """Triggers one active cycle evaluation check."""
    return await facade.execute_cycle()

@router.get("/live", status_code=status.HTTP_200_OK)
async def get_live_metrics(facade: ValidationFacade = Depends(get_validation_facade)):
    """Returns active portfolio drawdowns, daily losses, and validation status."""
    return await facade.execute_cycle()

@router.get("/performance", status_code=status.HTTP_200_OK)
async def get_performance_statistics(facade: ValidationFacade = Depends(get_validation_facade)):
    """Returns rolling return metrics (Sharpe, Sortino, Calmar)."""
    return facade.get_performance()

@router.get("/risk", status_code=status.HTTP_200_OK)
async def get_risk_statistics(facade: ValidationFacade = Depends(get_validation_facade)):
    """Returns risk concentration metrics and VaR(95) / CVaR(95) limits."""
    return facade.get_risk()

@router.get("/drift", status_code=status.HTTP_200_OK)
async def get_drift_statistics(facade: ValidationFacade = Depends(get_validation_facade)):
    """Returns population stability index (PSI) feature drift metrics."""
    return facade.get_drift()

@router.get("/scorecard", status_code=status.HTTP_200_OK)
async def get_scorecard_details(facade: ValidationFacade = Depends(get_validation_facade)):
    """Returns the generated validation_scorecard.json fields."""
    return facade.get_scorecard()
