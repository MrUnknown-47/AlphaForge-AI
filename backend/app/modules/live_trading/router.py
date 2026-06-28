from fastapi import APIRouter, Depends, status
from app.modules.live_trading.service import LiveTradingService

router = APIRouter(prefix="/live_trading", tags=["Live Signal Streaming Layer"])

def get_live_service() -> LiveTradingService:
    return LiveTradingService()

@router.post("/cycle", status_code=status.HTTP_200_OK)
async def trigger_live_cycle(service: LiveTradingService = Depends(get_live_service)):
    """Triggers one hourly trading prediction and order matching cycle."""
    await service.run_cycle()
    return {"status": "SUCCESS", "message": "Live hourly signal cycle completed."}

@router.get("/predictions", status_code=status.HTTP_200_OK)
async def get_live_predictions(service: LiveTradingService = Depends(get_live_service)):
    return service.get_predictions()

@router.get("/signals", status_code=status.HTTP_200_OK)
async def get_live_signals(service: LiveTradingService = Depends(get_live_service)):
    return service.get_signals()

@router.get("/metrics", status_code=status.HTTP_200_OK)
async def get_live_metrics(service: LiveTradingService = Depends(get_live_service)):
    return service.get_metrics()

@router.get("/alerts", status_code=status.HTTP_200_OK)
async def get_live_alerts(service: LiveTradingService = Depends(get_live_service)):
    return service.get_alerts()
