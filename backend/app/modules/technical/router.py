from fastapi import APIRouter, Depends, status
from app.modules.technical.facade import TechnicalFacade
from app.modules.technical.schemas import IndicatorCalculateRequest, IndicatorCalculateResponse, IndicatorsCacheResponse

router = APIRouter(prefix="/technical", tags=["Technical Analysis Features"])

@router.post("/calculate", response_model=IndicatorCalculateResponse)
async def calculate_custom_indicator(
    data: IndicatorCalculateRequest,
    facade: TechnicalFacade = Depends(get_technical_facade)
):
    results = await facade.compute_custom_indicator(data.ticker, data.indicator_name, data.parameters)
    return IndicatorCalculateResponse(
        ticker=data.ticker,
        indicator_name=data.indicator_name,
        timestamps=[], # Stub representation
        values=results
    )

@router.get("/cache/{ticker}", response_model=IndicatorsCacheResponse)
async def get_latest_cached_indicators(
    ticker: str,
    facade: TechnicalFacade = Depends(get_technical_facade)
):
    result = await facade.get_latest_indicators(ticker)
    if not result:
        return {}
    return result