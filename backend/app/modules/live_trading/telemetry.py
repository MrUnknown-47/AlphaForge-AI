def calculate_slippage_bps(arrival_price: float, fill_price: float, side: str) -> float:
    if arrival_price <= 0:
        return 0.0
    if side.upper() == "BUY":
        diff = fill_price - arrival_price
    else:
        diff = arrival_price - fill_price
    return (diff / arrival_price) * 10000.0

def calculate_implementation_shortfall(
    decision_price: float, fill_price: float, quantity: float, fees: float = 0.0
) -> float:
    # IS = (fill_price - decision_price) * quantity + fees
    return (fill_price - decision_price) * quantity + fees

def calculate_market_impact(qty: float, daily_volume: float = 1000000.0, vol_pct: float = 0.02) -> float:
    # Simulates temporary price impact proportional to square root of trade volume share
    if daily_volume <= 0:
        return 0.0
    return 0.5 * vol_pct * ((qty / daily_volume) ** 0.5)
