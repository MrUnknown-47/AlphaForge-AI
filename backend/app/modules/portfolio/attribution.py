from typing import Dict, List, Any
from app.modules.portfolio.exposure import SECTOR_MAP

def asset_contribution(positions: List[Dict[str, Any]], total_return: float) -> Dict[str, float]:
    total_val = sum(pos["market_value"] for pos in positions)
    if total_val == 0:
        return {}
    
    contrib = {}
    for pos in positions:
        weight = pos["market_value"] / total_val
        # Asset contribution = Weight * Asset return
        asset_ret = pos["unrealized_pct"]
        contrib[pos["symbol"]] = weight * asset_ret
    return contrib

def sector_contribution(positions: List[Dict[str, Any]], total_return: float) -> Dict[str, float]:
    total_val = sum(pos["market_value"] for pos in positions)
    if total_val == 0:
        return {}
    
    contrib = {}
    for pos in positions:
        sector = SECTOR_MAP.get(pos["symbol"].upper(), "Other")
        weight = pos["market_value"] / total_val
        asset_ret = pos["unrealized_pct"]
        contrib[sector] = contrib.get(sector, 0.0) + (weight * asset_ret)
    return contrib

def factor_contribution(positions: List[Dict[str, Any]]) -> Dict[str, float]:
    # Mocking standard Fama-French style factors contribution: market, size, value
    return {
        "Market (Beta)": 0.65,
        "Size (SMB)": 0.12,
        "Value (HML)": 0.08,
        "Idiosyncratic (Alpha)": 0.15
    }

def strategy_contribution(positions: List[Dict[str, Any]]) -> Dict[str, float]:
    return {
        "Trend Following": 0.45,
        "Mean Reversion": 0.30,
        "Arbitrage": 0.25
    }
