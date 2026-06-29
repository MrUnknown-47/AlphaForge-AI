from fastapi import APIRouter, status
from typing import Dict, Any, List
from app.modules.crypto.spot import CryptoSpotManager
from app.modules.crypto.perpetuals import CryptoPerpetualsManager
from app.modules.crypto.funding import CryptoFundingRateManager
from app.modules.crypto.risk import CryptoRiskEngine

router = APIRouter(prefix="/crypto", tags=["Crypto Trading Service"])
spot_eng = CryptoSpotManager()
perp_eng = CryptoPerpetualsManager()
funding_eng = CryptoFundingRateManager()
risk_eng = CryptoRiskEngine()

@router.get("")
async def list_crypto():
    return [
        {"symbol": "BTCUSD", "name": "Bitcoin Spot"},
        {"symbol": "ETHUSD", "name": "Ethereum Spot"},
        {"symbol": "SOLUSD", "name": "Solana Spot"}
    ]

@router.get("/funding")
async def get_funding(symbol: str):
    return {"symbol": symbol, "funding_rate_8h": funding_eng.get_funding_rate(symbol)}

@router.get("/liquidation")
async def get_liquidation(entry_price: float, leverage: float, is_long: bool):
    return {"liquidation_price": risk_eng.calculate_liquidation_price(entry_price, leverage, is_long)}
