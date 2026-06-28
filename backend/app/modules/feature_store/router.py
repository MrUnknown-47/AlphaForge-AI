from datetime import datetime
from fastapi import APIRouter, Depends, Query, status
from app.modules.feature_store.facade import FeatureStoreFacade
from app.modules.feature_store.dependencies import get_feature_store_facade
from app.modules.feature_store.schemas import BackfillRequest

router = APIRouter(prefix="/feature-store", tags=["Machine Learning Feature Store"])

@router.get("/online", status_code=status.HTTP_200_OK)
async def get_latest_features(
    tickers: list[str] = Query(..., description="Tickers to query"),
    facade: FeatureStoreFacade = Depends(get_feature_store_facade)
):
    return await facade.get_latest_online_features(tickers)

@router.post("/backfill", status_code=status.HTTP_202_ACCEPTED)
async def trigger_backfill_job(
    data: BackfillRequest,
    facade: FeatureStoreFacade = Depends(get_feature_store_facade)
):
    await facade.trigger_historical_backfill(data.tickers, data.start_date, data.end_date)
    return {"message": "Feature store backfilling task successfully accepted"}