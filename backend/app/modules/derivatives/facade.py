from typing import List, Dict, Any
from app.modules.derivatives.service import DerivativesService

class DerivativesFacade:
    def __init__(self, service: DerivativesService) -> None:
        self.service = service

    def get_surface(self, S: float) -> Dict[str, Any]:
        return self.service.get_options_surface(S)

    def get_greeks(self, S: float, K: float, T: float, r: float, sigma: float, option_type: str) -> Dict[str, float]:
        return self.service.calculate_greeks(S, K, T, r, sigma, option_type)

    def evaluate_strategy(self, name: str, **kwargs) -> Dict[str, Any]:
        return self.service.evaluate_strategy(name, **kwargs)

    def evaluate_futures_strategy(self, name: str, **kwargs) -> Dict[str, Any]:
        return self.service.evaluate_futures_strategy(name, **kwargs)

    def calculate_margin(self, method: str, positions: List[Dict[str, Any]]) -> Dict[str, float]:
        return self.service.calculate_margin(method, positions)

    def evaluate_risk(self, positions: List[Dict[str, Any]], returns: List[float]) -> Dict[str, Any]:
        return self.service.evaluate_risk(positions, returns)
