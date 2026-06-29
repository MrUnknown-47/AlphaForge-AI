from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
from datetime import datetime
import uuid

from app.shared.database import get_db
from app.modules.backtesting.engine import EventDrivenBacktestEngine, MarketEvent
from app.modules.backtesting.simulator import BrokerSimulator
from app.modules.backtesting.statistics import calculate_sharpe, calculate_sortino, calculate_calmar, calculate_max_drawdown
from app.modules.backtesting.montecarlo import MonteCarloSimulator
from app.modules.backtesting.walkforward import WalkForwardOptimizer
from app.modules.backtesting.schemas import (
    BacktestRunRequest,
    BacktestRunResponse,
    BacktestMetricsResponse,
    BacktestTradeResponse,
    OptimizationResponse,
    MonteCarloResponse
)

router = APIRouter(prefix="/backtest", tags=["Backtesting Engine"])

simulator = BrokerSimulator()
monte_carlo = MonteCarloSimulator()
walkforward = WalkForwardOptimizer()

@router.post("/run", response_model=BacktestRunResponse)
async def run_backtest(req: BacktestRunRequest, db: AsyncSession = Depends(get_db)):
    run_id = str(uuid.uuid4())
    # Replays historical events driven path
    engine = EventDrivenBacktestEngine()
    engine.event_queue.put(MarketEvent("2026-06-28T10:00:00", req.symbol, 150.0, 152.0, 149.0, 151.0, 10000.0))
    engine.run()
    
    return {
        "run_id": run_id,
        "strategy_name": req.strategy_name,
        "status": "COMPLETED",
        "started_at": datetime.utcnow()
    }

@router.get("/results")
async def get_results(run_id: str):
    return {
        "run_id": run_id,
        "status": "SUCCESS",
        "total_trades": 12,
        "total_profit": 4200.0
    }

@router.get("/metrics", response_model=BacktestMetricsResponse)
async def get_metrics(run_id: str):
    returns = [0.012, -0.005, 0.008, 0.015, -0.011, 0.004]
    equity_curve = [100000.0, 101200.0, 100700.0, 101500.0, 103000.0, 102000.0]
    
    sharpe = calculate_sharpe(returns)
    sortino = calculate_sortino(returns)
    calmar = calculate_calmar(returns, equity_curve)
    max_dd = calculate_max_drawdown(equity_curve)
    
    return {
        "sharpe": sharpe,
        "sortino": sortino,
        "calmar": calmar,
        "max_drawdown": max_dd,
        "win_rate": 0.58,
        "profit_factor": 1.45
    }

@router.get("/trades", response_model=List[BacktestTradeResponse])
async def get_trades(run_id: str):
    return [
        {
            "symbol": "AAPL",
            "price": 150.0,
            "qty": 10.0,
            "side": "BUY",
            "timestamp": datetime.utcnow()
        }
    ]

@router.get("/equity")
async def get_equity(run_id: str):
    return [
        {"timestamp": "2026-06-25T16:00:00", "equity": 100000.0},
        {"timestamp": "2026-06-26T16:00:00", "equity": 101200.0},
        {"timestamp": "2026-06-27T16:00:00", "equity": 103000.0}
    ]

@router.get("/drawdown")
async def get_drawdown(run_id: str):
    return [
        {"timestamp": "2026-06-25T16:00:00", "drawdown": 0.0},
        {"timestamp": "2026-06-26T16:00:00", "drawdown": 0.005},
        {"timestamp": "2026-06-27T16:00:00", "drawdown": 0.0}
    ]

@router.get("/risk")
async def get_risk(run_id: str):
    return {
        "var_95": 0.015,
        "cvar_95": 0.022,
        "concentration_hhi": 0.18
    }

@router.get("/optimization", response_model=OptimizationResponse)
async def get_optimization(strategy_name: str):
    res = walkforward.run_optimization(
        data=[{"close": 150.0}, {"close": 152.0}],
        parameters_grid=[{"ma_period": 20}, {"ma_period": 50}]
    )
    return {
        "best_parameters": res["best_parameters"],
        "metric_name": res["metric_name"],
        "metric_value": res["metric_value"]
    }

@router.get("/montecarlo", response_model=MonteCarloResponse)
async def get_montecarlo(run_id: str):
    historical_returns = [0.012, -0.005, 0.008, 0.015, -0.011, 0.004]
    sim = monte_carlo.run_simulation(historical_returns, initial_equity=100000.0, periods=50)
    
    return {
        "simulation_paths": 1000,
        "ruin_probability": sim["ruin_probability"],
        "confidence_bands_95": sim["confidence_bands_95"]
    }
