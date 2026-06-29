from typing import Dict, List, Any

# Map tickers to logical sectors for mock weight attributes
SECTOR_MAP = {
    "AAPL": "Technology",
    "MSFT": "Technology",
    "TSLA": "Consumer Cyclical",
    "SPY": "Index / ETF",
    "QQQ": "Index / ETF"
}

def calculate_exposure(positions: List[Dict[str, Any]], cash: float) -> float:
    total_value = sum(pos["market_value"] for pos in positions) + cash
    if total_value == 0:
        return 0.0
    return sum(pos["market_value"] for pos in positions) / total_value

def calculate_sector_weights(positions: List[Dict[str, Any]], cash: float) -> Dict[str, float]:
    total_val = sum(pos["market_value"] for pos in positions) + cash
    if total_val == 0:
        return {}
    
    weights = {}
    for pos in positions:
        sector = SECTOR_MAP.get(pos["symbol"].upper(), "Other")
        weights[sector] = weights.get(sector, 0.0) + (pos["market_value"] / total_val)
    
    weights["Cash"] = cash / total_val
    return weights

def calculate_asset_allocation(positions: List[Dict[str, Any]], cash: float) -> Dict[str, float]:
    total_val = sum(pos["market_value"] for pos in positions) + cash
    if total_val == 0:
        return {}
    
    alloc = {pos["symbol"]: pos["market_value"] / total_val for pos in positions}
    alloc["Cash"] = cash / total_val
    return alloc
