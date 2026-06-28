from typing import List, Dict, Any
from app.modules.derivatives.greeks_engine.service import GreeksService
from app.modules.derivatives.volatility_engine.service import VolatilityService
from app.modules.derivatives.strategies.service import OptionsStrategyService
from app.modules.derivatives.futures_engine.service import FuturesStrategyService
from app.modules.derivatives.margin_engine.service import MarginService
from app.modules.derivatives.risk_engine.service import RiskService

class DerivativesService:
    def __init__(self) -> None:
        pass

    def get_options_surface(self, S: float) -> Dict[str, Any]:
        return VolatilityService.generate_volatility_surface(S)

    def calculate_greeks(self, S: float, K: float, T: float, r: float, sigma: float, option_type: str) -> Dict[str, float]:
        return GreeksService.calculate_greeks(S, K, T, r, sigma, option_type)

    def evaluate_strategy(self, strategy_name: str, **kwargs) -> Dict[str, Any]:
        func = getattr(OptionsStrategyService, strategy_name.lower(), None)
        if func:
            return func(**kwargs)
        return {"error": f"Strategy {strategy_name} not found"}

    def evaluate_futures_strategy(self, strategy_name: str, **kwargs) -> Dict[str, Any]:
        func = getattr(FuturesStrategyService, strategy_name.lower(), None)
        if func:
            return func(**kwargs)
        return {"error": f"Futures strategy {strategy_name} not found"}

    def calculate_margin(self, method: str, positions: List[Dict[str, Any]]) -> Dict[str, float]:
        if method.upper() == "REG-T":
            return MarginService.calculate_reg_t(positions)
        elif method.upper() == "PORTFOLIO":
            return MarginService.calculate_portfolio_margin(positions)
        elif method.upper() == "SPAN":
            return MarginService.calculate_span_approximation(positions)
        return {"error": f"Method {method} not supported"}

    def evaluate_risk(self, positions: List[Dict[str, Any]], returns: List[float]) -> Dict[str, Any]:
        return {
            "var_cvar": RiskService.calculate_var_cvar(returns),
            "greeks_exposure": RiskService.calculate_greeks_exposure(positions),
            "stress_tests": RiskService.perform_stress_tests(positions)
        }
