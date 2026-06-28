from fastapi import APIRouter, Depends, status, Query
from typing import Dict, Any, List
from app.modules.derivatives.facade import DerivativesFacade
from app.modules.derivatives.service import DerivativesService

router = APIRouter(prefix="/derivatives", tags=["Derivatives"])

def get_derivatives_facade() -> DerivativesFacade:
    return DerivativesFacade(DerivativesService())

@router.get("/volatility")
async def get_volatility_surface(
    underlying_price: float = Query(100.0),
    facade: DerivativesFacade = Depends(get_derivatives_facade)
):
    return facade.get_surface(underlying_price)

@router.get("/greeks")
async def get_option_greeks(
    S: float = Query(100.0),
    K: float = Query(100.0),
    T: float = Query(0.25),
    r: float = Query(0.05),
    sigma: float = Query(0.2),
    option_type: str = Query("CALL"),
    facade: DerivativesFacade = Depends(get_derivatives_facade)
):
    return facade.get_greeks(S, K, T, r, sigma, option_type)

@router.post("/strategies")
async def evaluate_strategy(
    strategy_name: str,
    parameters: Dict[str, Any],
    facade: DerivativesFacade = Depends(get_derivatives_facade)
):
    # Determine options or futures strategy
    if strategy_name.lower() in ["directional", "calendar_spread", "basis_trading", "carry_trading", "hedging"]:
        return facade.evaluate_futures_strategy(strategy_name, **parameters)
    return facade.evaluate_strategy(strategy_name, **parameters)

@router.post("/risk")
async def evaluate_portfolio_risk(
    payload: Dict[str, Any],
    facade: DerivativesFacade = Depends(get_derivatives_facade)
):
    positions = payload.get("positions", [])
    returns = payload.get("returns", [])
    return facade.evaluate_risk(positions, returns)

@router.post("/margin")
async def calculate_portfolio_margin(
    payload: Dict[str, Any],
    facade: DerivativesFacade = Depends(get_derivatives_facade)
):
    method = payload.get("method", "REG-T")
    positions = payload.get("positions", [])
    return facade.calculate_margin(method, positions)
