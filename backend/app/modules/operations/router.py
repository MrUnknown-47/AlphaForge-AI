from fastapi import APIRouter, Depends, status
from app.modules.operations.facade import OperationsFacade

router = APIRouter(prefix="/ops", tags=["Operations Platform Gateway"])

def get_ops_facade() -> OperationsFacade:
    return OperationsFacade()

@router.get("/health", status_code=status.HTTP_200_OK)
async def get_ops_health(facade: OperationsFacade = Depends(get_ops_facade)):
    """Returns active service uptime, latency, and socket connectivities."""
    return facade.get_health()

@router.get("/models", status_code=status.HTTP_200_OK)
async def get_ops_models(facade: OperationsFacade = Depends(get_ops_facade)):
    """Returns rolling accuracy, feature shifts, and model staleness parameters."""
    return facade.get_models()

@router.get("/portfolio", status_code=status.HTTP_200_OK)
async def get_ops_portfolio(facade: OperationsFacade = Depends(get_ops_facade)):
    """Returns leverage limits, CVaR and portfolio beta metrics."""
    return facade.get_portfolio()

@router.get("/incidents", status_code=status.HTTP_200_OK)
async def get_ops_incidents(facade: OperationsFacade = Depends(get_ops_facade)):
    """Returns recorded P0/P1/P2 operational incident logs."""
    return facade.get_incidents()

@router.get("/alerts", status_code=status.HTTP_200_OK)
async def get_ops_alerts(facade: OperationsFacade = Depends(get_ops_facade)):
    """Returns real-time warning logs from operations monitoring."""
    return facade.get_alerts()

@router.get("/audit", status_code=status.HTTP_200_OK)
async def get_ops_audit(facade: OperationsFacade = Depends(get_ops_facade)):
    """Returns file paths of serialized immutable transaction audit trails."""
    return facade.get_audit()

@router.get("/scorecard", status_code=status.HTTP_200_OK)
async def get_ops_scorecard(facade: OperationsFacade = Depends(get_ops_facade)):
    """Returns operations_scorecard.json fields including ready flags."""
    return facade.get_scorecard()
