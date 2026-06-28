from fastapi import APIRouter, Depends, status
from app.modules.broker.facade import BrokerFacade

router = APIRouter(prefix="/broker", tags=["Broker Integration Layer"])

def get_broker_facade() -> BrokerFacade:
    return BrokerFacade()

@router.get("/account", status_code=status.HTTP_200_OK)
async def get_account_details(facade: BrokerFacade = Depends(get_broker_facade)):
    """Returns active broker account summary."""
    return await facade.get_account()

@router.get("/positions", status_code=status.HTTP_200_OK)
async def get_open_positions(facade: BrokerFacade = Depends(get_broker_facade)):
    """Returns open positions from the active broker."""
    return await facade.get_positions()
