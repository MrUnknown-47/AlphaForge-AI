from typing import List

class ComplianceControlsManager:
    def __init__(self) -> None:
        self.restricted_list = ["XYZ", "BAD_STOCK"]
        self.watch_list = ["TSLA", "AAPL"]

    def verify_symbol(self, symbol: str) -> bool:
        return symbol not in self.restricted_list
