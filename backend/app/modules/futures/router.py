from fastapi import APIRouter, status
from typing import Dict, Any, List
from app.modules.futures.contracts import FuturesContractsManager
from app.modules.futures.margin import FuturesMarginEngine
from app.modules.futures.rollover import FuturesRolloverEngine
from app.modules.futures.exposure import FuturesExposureTracker

router = APIRouter(prefix="/futures", tags=["Futures Trading Service"])
contracts = FuturesContractsManager()
margin_eng = FuturesMarginEngine()
roll_eng = FuturesRolloverEngine()
exposure_eng = FuturesExposureTracker()

@router.get("")
async def list_futures():
    return [
        {"symbol": "ES_U26", "name": "E-mini S&P 500 September 2026", "multiplier": 50},
        {"symbol": "NQ_U26", "name": "E-mini Nasdaq 100 September 2026", "multiplier": 20},
        {"symbol": "CL_V26", "name": "Crude Oil October 2026", "multiplier": 1000}
    ]

@router.post("/roll", status_code=status.HTTP_200_OK)
async def post_roll(current_symbol: str, next_symbol: str, quantity: float):
    res = roll_eng.perform_rollover(current_symbol, next_symbol, quantity)
    return res

@router.get("/margin")
async def get_margin(symbol: str, quantity: float):
    return margin_eng.calculate_margin(symbol, quantity)

@router.get("/exposure")
async def get_exposure(symbol: str, price: float, quantity: float, multiplier: float):
    return exposure_eng.calculate_exposure(symbol, price, quantity, multiplier)
