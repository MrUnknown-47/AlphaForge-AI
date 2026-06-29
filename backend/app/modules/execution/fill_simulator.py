from app.modules.execution.slippage_engine import SlippageEngine

class FillSimulator:
    def __init__(self) -> None:
        self.slippage = SlippageEngine()

    def simulate_fill(self, base_price: float, side: str, quantity: float) -> float:
        # Defaults to 1M daily volume for standard large-caps
        return self.slippage.get_fill_price(base_price, side, quantity, avg_volume_1d=1000000.0)
