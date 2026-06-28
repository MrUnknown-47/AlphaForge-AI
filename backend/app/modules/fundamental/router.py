from fastapi import APIRouter, Depends, Query, status
from app.modules.fundamental.facade import FundamentalFacade
from app.modules.fundamental.service import FundamentalService
from app.modules.fundamental.dependencies import get_fundamental_facade, get_fundamental_service
from app.modules.fundamental.schemas import FinancialStatementResponse

router = APIRouter(prefix="/fundamental", tags=["Fundamental Analysis Features"])

@router.get("/statements/{ticker}", response_model=list[FinancialStatementResponse])
async def get_statements(
    ticker: str,
    limit: int = Query(20, description="Number of statements to retrieve"),
    facade: FundamentalFacade = Depends(get_fundamental_facade)
):
    return await facade.get_quarterly_statements(ticker, limit)

@router.post("/sync/{ticker}", status_code=status.HTTP_202_ACCEPTED)
async def sync_ticker_data(
    ticker: str,
    service: FundamentalService = Depends(get_fundamental_service)
):
    # Triggers on-demand sync of fundamentals
    await service.sync_ticker_fundamentals(ticker, limit=2)
    return {"message": f"Sync job executed successfully for {ticker}"}