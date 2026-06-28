from fastapi import APIRouter, Depends, status
from app.modules.security.facade import SecurityFacade

router = APIRouter(prefix="/security", tags=["Security and Governance Gateway"])

def get_security_facade() -> SecurityFacade:
    return SecurityFacade()

@router.get("/status", status_code=status.HTTP_200_OK)
async def get_security_status(facade: SecurityFacade = Depends(get_security_facade)):
    """Returns trading enabled status, active kill switch and broker modes."""
    return facade.get_status()

@router.get("/audit", status_code=status.HTTP_200_OK)
async def get_audit_trail(facade: SecurityFacade = Depends(get_security_facade)):
    """Returns recorded security logs trails."""
    return facade.get_audit()

@router.get("/anomalies", status_code=status.HTTP_200_OK)
async def get_anomalies_logs(facade: SecurityFacade = Depends(get_security_facade)):
    """Returns detected latency spikes, login attempts anomalies."""
    return facade.get_anomalies()

@router.get("/kill-switch", status_code=status.HTTP_200_OK)
async def get_kill_switch_state(facade: SecurityFacade = Depends(get_security_facade)):
    """Returns active state of global system kill switch."""
    return facade.get_kill_switch_state()

@router.get("/capital", status_code=status.HTTP_200_OK)
async def get_capital_limits(facade: SecurityFacade = Depends(get_security_facade)):
    """Returns order sizes limits configurations."""
    return facade.get_capital()

@router.get("/secrets", status_code=status.HTTP_200_OK)
async def get_masked_secrets(facade: SecurityFacade = Depends(get_security_facade)):
    """Returns list of masked system keys."""
    return facade.get_secrets()

@router.get("/scorecard", status_code=status.HTTP_200_OK)
async def get_security_scorecard(facade: SecurityFacade = Depends(get_security_facade)):
    """Returns security_scorecard.json fields including validation flags."""
    return facade.get_scorecard()
