from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any

from app.shared.database import get_db
from app.modules.portfolio.synchronizer import PortfolioSynchronizer
from app.modules.portfolio.exposure import calculate_exposure, calculate_sector_weights, calculate_asset_allocation
from app.modules.portfolio.analytics import calculate_sharpe, calculate_sortino, calculate_calmar, calculate_volatility
from app.modules.portfolio.risk import calculate_var, calculate_cvar, calculate_leverage, calculate_concentration
from app.modules.portfolio.attribution import asset_contribution, factor_contribution, strategy_contribution
from app.modules.portfolio.cache import PortfolioCache
from app.modules.portfolio.schemas import (
    AccountSyncResponse,
    PositionSyncResponse,
    AllocationResponse,
    ExposureResponse,
    RiskResponse,
    AttributionResponse
)

router = APIRouter(prefix="/portfolio", tags=["Portfolio Sync & Analytics"])

sync_engine = PortfolioSynchronizer()
cache = PortfolioCache()

@router.post("/sync")
async def sync_portfolio(db: AsyncSession = Depends(get_db)):
    acc = await sync_engine.sync_account(db)
    positions = await sync_engine.sync_positions(db)
    orders = await sync_engine.sync_orders(db)
    return {"status": "synchronized", "account": acc, "positions": positions, "orders": orders}

@router.get("/account", response_model=AccountSyncResponse)
async def get_account(db: AsyncSession = Depends(get_db)):
    cache_key = "portfolio:account:latest"
    cached = cache.get(cache_key)
    if cached:
        return cached

    acc = await sync_engine.sync_account(db)
    cache.set(cache_key, acc, ttl=5)
    return acc

@router.get("/positions", response_model=List[PositionSyncResponse])
async def get_positions(db: AsyncSession = Depends(get_db)):
    cache_key = "portfolio:positions:latest"
    cached = cache.get(cache_key)
    if cached:
        return cached

    positions = await sync_engine.sync_positions(db)
    cache.set(cache_key, positions, ttl=5)
    return positions

@router.get("/orders")
async def get_orders(db: AsyncSession = Depends(get_db)):
    return await sync_engine.sync_orders(db)

@router.get("/history")
async def get_history():
    # Return simulated portfolio value timeline
    return [
        {"timestamp": "2026-06-25T16:00:00", "equity": 98500.0, "cash": 45000.0},
        {"timestamp": "2026-06-26T16:00:00", "equity": 99100.0, "cash": 42000.0},
        {"timestamp": "2026-06-27T16:00:00", "equity": 100000.0, "cash": 40000.0}
    ]

@router.get("/allocation")
async def get_allocation(db: AsyncSession = Depends(get_db)):
    positions = await sync_engine.sync_positions(db)
    acc = await sync_engine.sync_account(db)
    return calculate_asset_allocation(positions, acc["cash"])

@router.get("/exposure", response_model=ExposureResponse)
async def get_exposure(db: AsyncSession = Depends(get_db)):
    positions = await sync_engine.sync_positions(db)
    acc = await sync_engine.sync_account(db)
    
    total_exp = calculate_exposure(positions, acc["cash"])
    sec_weights = calculate_sector_weights(positions, acc["cash"])
    asset_alloc = calculate_asset_allocation(positions, acc["cash"])
    
    return {
        "total_exposure": total_exp,
        "sector_allocations": sec_weights,
        "asset_allocations": asset_alloc
    }

@router.get("/risk", response_model=RiskResponse)
async def get_risk(db: AsyncSession = Depends(get_db)):
    cache_key = "portfolio:risk:latest"
    cached = cache.get(cache_key)
    if cached:
        return cached

    positions = await sync_engine.sync_positions(db)
    acc = await sync_engine.sync_account(db)
    
    # Standard simulated returns path for VaR
    mock_returns = [0.012, -0.005, 0.008, 0.015, -0.011, 0.004, -0.002, 0.009, 0.001, -0.006]
    var_95 = calculate_var(mock_returns, 0.95)
    cvar_95 = calculate_cvar(mock_returns, 0.95)
    leverage = calculate_leverage(acc["equity"], acc["portfolio_value"])
    concentration = calculate_concentration(positions)
    
    res = {
        "var_95": var_95,
        "cvar_95": cvar_95,
        "leverage": leverage,
        "concentration_index": concentration
    }
    cache.set(cache_key, res, ttl=30)
    return res

@router.get("/performance")
async def get_performance(db: AsyncSession = Depends(get_db)):
    # Returns relative benchmark comparisons
    return {
        "portfolio_ytd": 0.145,
        "benchmark_ytd": 0.112,
        "outperformance": 0.033
    }

@router.get("/analytics")
async def get_analytics(db: AsyncSession = Depends(get_db)):
    cache_key = "portfolio:analytics:latest"
    cached = cache.get(cache_key)
    if cached:
        return cached

    # Sharpe / Sortino metrics calculations
    mock_returns = [0.012, -0.005, 0.008, 0.015, -0.011, 0.004, -0.002, 0.009, 0.001, -0.006]
    equity_curve = [98500.0, 99100.0, 100000.0]
    
    sharpe = calculate_sharpe(mock_returns)
    sortino = calculate_sortino(mock_returns)
    calmar = calculate_calmar(mock_returns, equity_curve)
    vol = calculate_volatility(mock_returns)
    
    res = {
        "sharpe_ratio": sharpe,
        "sortino_ratio": sortino,
        "calmar_ratio": calmar,
        "annualized_volatility": vol
    }
    cache.set(cache_key, res, ttl=60)
    return res
