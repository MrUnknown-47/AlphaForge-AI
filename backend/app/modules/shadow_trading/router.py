from fastapi import APIRouter, Depends, status
from app.modules.shadow_trading.facade import ShadowTradingFacade

router = APIRouter(prefix="/shadow", tags=["Alpaca Paper Shadow Trading Gateway"])

def get_shadow_facade() -> ShadowTradingFacade:
    return ShadowTradingFacade()

@router.post("/reconcile", status_code=status.HTTP_200_OK)
async def trigger_reconciliation(facade: ShadowTradingFacade = Depends(get_shadow_facade)):
    """Triggers hourly position reconciliation cycle against Alpaca Paper API."""
    return await facade.execute_reconciliation()

@router.get("/account", status_code=status.HTTP_200_OK)
async def get_shadow_account(facade: ShadowTradingFacade = Depends(get_shadow_facade)):
    """Returns active broker cash balances, buying power, and halt flags status."""
    return facade.get_account()

@router.get("/positions", status_code=status.HTTP_200_OK)
async def get_shadow_positions(facade: ShadowTradingFacade = Depends(get_shadow_facade)):
    """Returns open positions from the shadow portfolio."""
    return facade.get_positions()

@router.get("/performance", status_code=status.HTTP_200_OK)
async def get_performance_statistics(facade: ShadowTradingFacade = Depends(get_shadow_facade)):
    """Returns rolling returns performance metrics."""
    return facade.get_performance()

@router.get("/execution", status_code=status.HTTP_200_OK)
async def get_execution_metrics(facade: ShadowTradingFacade = Depends(get_shadow_facade)):
    """Returns slippage, spread, latency, and fill percentages metrics."""
    return facade.get_execution()

@router.get("/reconciliation", status_code=status.HTTP_200_OK)
async def get_reconciliation_details(facade: ShadowTradingFacade = Depends(get_shadow_facade)):
    """Returns results of the last position reconciliations check."""
    return await facade.execute_reconciliation()

@router.get("/validation", status_code=status.HTTP_200_OK)
async def get_validation_metrics(facade: ShadowTradingFacade = Depends(get_shadow_facade)):
    """Returns CAGR, Sharpe, and model stability thresholds metrics."""
    return facade.get_performance()
