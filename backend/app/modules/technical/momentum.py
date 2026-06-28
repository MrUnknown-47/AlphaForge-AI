from app.modules.technical.indicators import TechnicalIndicator, IndicatorRegistry

@IndicatorRegistry.register("RSI")
class RelativeStrengthIndex(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        # RSI calculation stub
        period = self.params.get("period", 14)
        return [50.0] * len(ohlcv_data)

@IndicatorRegistry.register("ROC")
class RateOfChange(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [0.0] * len(ohlcv_data)

@IndicatorRegistry.register("MOM")
class Momentum(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [0.0] * len(ohlcv_data)

@IndicatorRegistry.register("STOCHASTIC")
class StochasticOscillator(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[dict[str, float]]:
        # Returns %K and %D lines
        return [{"k": 80.0, "d": 78.0}] * len(ohlcv_data)
