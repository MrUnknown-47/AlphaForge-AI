from fastapi import APIRouter, HTTPException, status
from typing import Dict, Any, List
from app.modules.assets.security_master import SecurityMaster
from app.modules.assets.schemas import AssetSpecsResponse

router = APIRouter(prefix="/assets", tags=["Multi-Asset Security Master Service"])
master = SecurityMaster()

@router.get("", response_model=List[AssetSpecsResponse])
async def list_assets():
    res = []
    for symbol, details in master.assets.items():
        res.append({
            "symbol": symbol,
            "asset_type": details.get("type", "EQUITY"),
            "exchange": details.get("exchange", "NASDAQ"),
            "tick_size": details.get("tick_size", 0.01),
            "multiplier": details.get("multiplier", 1.0),
            "currency": details.get("currency", "USD"),
            "margin_requirement": details.get("margin_requirement", 0.50)
        })
    return res

@router.get("/{symbol}", response_model=AssetSpecsResponse)
async def get_asset(symbol: str):
    details = master.get_security_details(symbol)
    if not details:
        raise HTTPException(status_code=404, detail="Asset not found in Security Master")
    return {
        "symbol": symbol,
        "asset_type": details.get("type", "EQUITY"),
        "exchange": details.get("exchange", "NASDAQ"),
        "tick_size": details.get("tick_size", 0.01),
        "multiplier": details.get("multiplier", 1.0),
        "currency": details.get("currency", "USD"),
        "margin_requirement": details.get("margin_requirement", 0.50)
    }

@router.post("", status_code=status.HTTP_201_CREATED)
async def register_asset(symbol: str, asset_type: str, exchange: str, tick_size: float, multiplier: float, currency: str, margin_requirement: float):
    details = {
        "type": asset_type,
        "exchange": exchange,
        "tick_size": tick_size,
        "multiplier": multiplier,
        "currency": currency,
        "margin_requirement": margin_requirement
    }
    master.add_security(symbol, details)
    return {"status": "CREATED", "symbol": symbol}
