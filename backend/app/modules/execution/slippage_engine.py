class SlippageEngine:
    def __init__(self, base_spread_bps: float = 2.0, market_impact_coef: float = 0.1) -> None:
        self.base_spread_bps = base_spread_bps
        self.market_impact_coef = market_impact_coef

    def calculate_slippage(self, quantity: float, avg_volume_1d: float) -> float:
        # Standard slippage = base spread + market impact
        # Market impact scale is proportional to (quantity / daily volume) ^ 0.5
        if avg_volume_1d <= 0:
            return 0.0
        impact = self.market_impact_coef * ((quantity / avg_volume_1d) ** 0.5)
        total_bps = self.base_spread_bps + (impact * 10000.0)
        return total_bps / 10000.0

    def get_fill_price(self, base_price: float, side: str, quantity: float, avg_volume_1d: float = 1000000.0) -> float:
        slippage_pct = self.calculate_slippage(quantity, avg_volume_1d)
        if side.upper() == "BUY":
            return base_price * (1.0 + slippage_pct)
        else:
            return base_price * (1.0 - slippage_pct)
