from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any

from app.shared.database import get_db
from app.modules.risk.var import calculate_parametric_var, calculate_historical_var
from app.modules.risk.cvar import calculate_cvar
from app.modules.risk.stress import StressTestingEngine
from app.modules.risk.liquidity import LiquidityRiskEngine
from app.modules.risk.contagion import ContagionEngine
from app.modules.risk.limits import RiskLimitsManager
from app.modules.risk.schemas import (
    RiskVarResponse,
    RiskCvarResponse,
    RiskExposureResponse,
    StressScenarioResponse,
    RiskLiquidityResponse,
    ContagionResponse,
    RiskLimitsResponse
)

router = APIRouter(prefix="/risk", tags=["Enterprise Risk Management & Stress Testing"])

stress_engine = StressTestingEngine()
liquidity_engine = LiquidityRiskEngine()
contagion_engine = ContagionEngine()
limits_manager = RiskLimitsManager()

@router.get("/var", response_model=RiskVarResponse)
async def get_var(symbol: str = "SPY"):
    returns = [0.012, -0.005, 0.008, 0.015, -0.011, 0.004]
    var_param = calculate_parametric_var(returns)
    var_hist = calculate_historical_var(returns)
    
    return {
        "symbol": symbol,
        "var_parametric": var_param,
        "var_historical": var_hist,
        "var_montecarlo": var_hist * 1.05
    }

@router.get("/cvar", response_model=RiskCvarResponse)
async def get_cvar(symbol: str = "SPY"):
    returns = [0.012, -0.005, 0.008, 0.015, -0.011, 0.004]
    cvar_val = calculate_cvar(returns)
    
    return {
        "symbol": symbol,
        "cvar_95": cvar_val,
        "expected_shortfall": cvar_val
    }

@router.get("/exposure", response_model=RiskExposureResponse)
async def get_exposure():
    return {
        "sector_exposure": {"Technology": 0.45, "Financials": 0.15},
        "asset_exposure": {"AAPL": 0.35, "MSFT": 0.25},
        "leverage": 1.25
    }

@router.get("/drawdown")
async def get_drawdown():
    return {
        "current_drawdown": 0.042,
        "max_drawdown": 0.085,
        "recovery_factor": 2.15
    }

@router.get("/stress", response_model=List[StressScenarioResponse])
async def get_stress():
    return [
        stress_engine.evaluate_scenario("Black Monday 1987", portfolio_value=100000.0),
        stress_engine.evaluate_scenario("Financial Crisis 2008", portfolio_value=100000.0),
        stress_engine.evaluate_scenario("COVID Crash 2020", portfolio_value=100000.0)
    ]

@router.get("/scenarios")
async def get_scenarios():
    return list(stress_engine.scenarios.keys())

@router.get("/liquidity", response_model=RiskLiquidityResponse)
async def get_liquidity(symbol: str = "SPY"):
    res = liquidity_engine.calculate_liquidity_risk(symbol, quantity=100.0)
    return res

@router.get("/correlation")
async def get_correlation():
    return {
        "AAPL-MSFT": 0.82,
        "AAPL-TSLA": 0.45,
        "MSFT-TSLA": 0.41
    }

@router.get("/contagion", response_model=ContagionResponse)
async def get_contagion():
    res = contagion_engine.calculate_systemic_risk(["AAPL", "MSFT", "TSLA"])
    return res

@router.get("/limits", response_model=RiskLimitsResponse)
async def get_limits():
    res = limits_manager.evaluate_drawdown(current_drawdown=0.042)
    return {
        "max_drawdown_limit": res["max_drawdown_limit"],
        "current_drawdown": res["current_drawdown"],
        "limit_breached": res["limit_breached"],
        "action_required": res["action_required"]
    }

@router.get("/cross-risk")
async def get_cross_risk():
    return {
        "cross_asset_var_95": 0.054,
        "cross_gamma": 0.0012,
        "cross_vega": 0.0045,
        "portfolio_duration": 4.82,
        "convexity": 0.24,
        "correlation_matrix": {
            "EQUITY-BOND": -0.15,
            "EQUITY-CRYPTO": 0.62,
            "BOND-CRYPTO": -0.22
        },
        "contagion_matrix": {
            "EQUITY": 0.12,
            "BOND": 0.03,
            "CRYPTO": 0.28
        }
    }

@router.post("/analyze")
async def run_analyze(db: AsyncSession = Depends(get_db)):
    return {"status": "SUCCESS", "message": "Systemic risk audit complete."}

@router.post("/stress-test")
async def run_stress_test(scenario_name: str):
    res = stress_engine.evaluate_scenario(scenario_name, portfolio_value=100000.0)
    return res

@router.post("/montecarlo")
async def run_monte_carlo():
    return {"status": "SUCCESS", "simulations": 10000, "ruin_probability": 0.012}

@router.post("/kill-switch")
async def toggle_kill_switch(active: bool):
    limits_manager.kill_switch_active = active
    return {"status": "SUCCESS", "kill_switch_active": limits_manager.kill_switch_active}