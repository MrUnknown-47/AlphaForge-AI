from abc import ABC, abstractmethod
from typing import Any
from app.modules.technical.exceptions import IndicatorNotFoundException

class TechnicalIndicator(ABC):
    def __init__(self, parameters: dict[str, Any]) -> None:
        self.params = parameters

    @abstractmethod
    def calculate(self, ohlcv_data: list[dict]) -> list[float | dict[str, float]]:
        """
        Calculation signature.
        Inputs: List of dicts representing OHLCV data.
        Outputs: List of calculated values (float or dictionaries of metrics).
        """
        pass

class IndicatorRegistry:
    _registry: dict[str, type[TechnicalIndicator]] = {}

    @classmethod
    def register(cls, name: str) -> Any:
        def decorator(indicator_class: type[TechnicalIndicator]) -> type[TechnicalIndicator]:
            cls._registry[name.upper()] = indicator_class
            return indicator_class
        return decorator

    @classmethod
    def get(cls, name: str) -> type[TechnicalIndicator]:
        indicator_class = cls._registry.get(name.upper())
        if not indicator_class:
            raise IndicatorNotFoundException(f"Indicator '{name}' is not registered")
        return indicator_class

class IndicatorFactory:
    @staticmethod
    def create(name: str, parameters: dict[str, Any]) -> TechnicalIndicator:
        indicator_class = IndicatorRegistry.get(name)
        return indicator_class(parameters)
