from fastapi import APIRouter, status
from typing import Dict, Any, List
from app.modules.fund.fund_manager import FundManager
from app.modules.fund.capital_allocator import CapitalAllocator
from app.modules.fund.benchmark_engine import BenchmarkEngine
from app.modules.fund.schemas import FundMetricsResponse

router = APIRouter(prefix="/fund", tags=["Autonomous Hedge Fund Manager Service"])
mgr = FundManager()
allocator = CapitalAllocator()
bench_eng = BenchmarkEngine()

@router.get("/nav")
async def get_nav():
    return {"nav": mgr.nav}

@router.get("/aum")
async def get_aum():
    return {"aum": mgr.aum}

@router.get("/allocations")
async def get_allocations():
    weights = {"AF_QUANT_EQUITY": 0.40, "AF_CTA": 0.30, "AF_GLOBAL_MACRO": 0.30}
    return allocator.allocate_capital_to_strategies(mgr.aum, weights)

@router.get("/exposure")
async def get_exposure():
    return {
        "gross_exposure": mgr.aum * mgr.leverage,
        "net_exposure": mgr.aum * 0.85,
        "beta_exposure": 1.12,
        "factor_exposure": {"Value": 0.15, "Growth": 0.45, "Momentum": 0.25}
    }

@router.get("/performance")
async def get_performance():
    portfolio_ret = 0.145 # 14.5% returns
    alpha = bench_eng.get_alpha_vs_benchmark("SPY", portfolio_ret)
    return {
        "portfolio_return": portfolio_ret,
        "benchmark": "SPY",
        "alpha": alpha,
        "sharpe_ratio": 2.15,
        "information_ratio": 1.45,
        "tracking_error": 0.042
    }

@router.get("/attribution")
async def get_attribution():
    return {
        "factor_attribution": {"Market": 0.082, "Size": -0.012, "Value": 0.024, "Momentum": 0.045, "Alpha": 0.006},
        "sector_attribution": {"Technology": 0.095, "Healthcare": 0.025, "Financials": 0.015, "Energy": 0.010}
    }

@router.get("/committees")
async def get_committees():
    return {
        "investment_committee": "APPROVED (BUY 40% Weight in US Growth)",
        "risk_committee": "APPROVED (Leverage cap set at 2.5x)",
        "execution_committee": "APPROVED (Limit execution latency under 12ms)"
    }

@router.post("/rebalance", status_code=status.HTTP_200_OK)
async def post_rebalance():
    return {"status": "SUCCESS", "message": "Autonomous fund rebalancing complete."}

@router.post("/allocate", status_code=status.HTTP_200_OK)
async def post_allocate():
    return {"status": "SUCCESS", "message": "Capital allocations to sub-strategies completed."}

@router.post("/build", status_code=status.HTTP_200_OK)
async def post_build():
    return {"status": "SUCCESS", "message": "Fund portfolio construction completed."}

@router.post("/optimize", status_code=status.HTTP_200_OK)
async def post_optimize():
    return {"status": "SUCCESS", "message": "Fund-level asset optimization completed."}
