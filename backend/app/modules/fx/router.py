from fastapi import APIRouter, status
from typing import Dict, Any
from app.modules.fx.currency_pairs import CurrencyPairsManager
from app.modules.fx.carry import ForexCarryCalculator
from app.modules.fx.hedging import ForexHedgingEngine

router = APIRouter(prefix="/fx", tags=["Forex Trading Service"])
pairs = CurrencyPairsManager()
carry_calc = ForexCarryCalculator()
hedge_eng = ForexHedgingEngine()

@router.get("")
async def list_forex():
    return [
        {"symbol": "EURUSD", "base": "EUR", "quote": "USD"},
        {"symbol": "USDJPY", "base": "USD", "quote": "JPY"},
        {"symbol": "GBPUSD", "base": "GBP", "quote": "USD"}
    ]

@router.get("/carry")
async def get_carry(pair: str, is_long: bool):
    return {"pair": pair, "annualized_carry_yield": carry_calc.calculate_carry_rate(pair, is_long)}

@router.post("/hedge", status_code=status.HTTP_200_OK)
async def post_hedge(foreign_currency_exposure: float, spot_price: float):
    return hedge_eng.calculate_hedging_shares(foreign_currency_exposure, spot_price)
