import uuid
from fastapi import APIRouter, Depends, status, Query
from app.modules.portfolio.facade import PortfolioFacade
from app.modules.portfolio.service import PortfolioService
from app.modules.portfolio.dependencies import get_portfolio_facade, get_portfolio_service
from app.modules.portfolio.schemas import (
    PortfolioCreate,
    PortfolioResponse,
    TransactionCreate,
    TransactionResponse,
    PortfolioValuationResponse,
)

router = APIRouter(prefix="/portfolios", tags=["Portfolio Management"])

@router.post("/", response_model=PortfolioResponse, status_code=status.HTTP_201_CREATED)
async def create_portfolio(
    data: PortfolioCreate,
    # Simulate current user injection
    user_id: uuid.UUID = Query(..., description="Simulated active user UUID"),
    service: PortfolioService = Depends(get_portfolio_service)
):
    return await service.create_portfolio(user_id, data.name)

@router.post("/{portfolio_id}/deposit", response_model=TransactionResponse)
async def deposit_cash(
    portfolio_id: uuid.UUID,
    data: TransactionCreate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    return await service.execute_deposit(portfolio_id, data.amount)

@router.post("/{portfolio_id}/withdraw", response_model=TransactionResponse)
async def withdraw_cash(
    portfolio_id: uuid.UUID,
    data: TransactionCreate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    return await service.execute_withdraw(portfolio_id, data.amount)

@router.get("/{portfolio_id}/valuation", response_model=PortfolioValuationResponse)
async def get_valuation(
    portfolio_id: uuid.UUID,
    facade: PortfolioFacade = Depends(get_portfolio_facade)
):
    return await facade.get_portfolio_valuation(portfolio_id)