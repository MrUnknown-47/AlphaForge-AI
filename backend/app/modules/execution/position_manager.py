from typing import Dict, Any

class PositionManager:
    def __init__(self) -> None:
        self.positions: Dict[str, float] = {}

    def update_position(self, ticker: str, quantity: float, side: str) -> None:
        current = self.positions.get(ticker, 0.0)
        if side.upper() == "BUY":
            self.positions[ticker] = current + quantity
        else:
            self.positions[ticker] = current - quantity
            if self.positions[ticker] <= 0:
                self.positions.pop(ticker, None)

    def get_position_size(self, ticker: str) -> float:
        return self.positions.get(ticker, 0.0)
