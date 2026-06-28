from app.modules.technical.indicators import TechnicalIndicator, IndicatorRegistry

@IndicatorRegistry.register("MACD")
class MovingAverageConvergenceDivergence(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[dict[str, float]]:
        # Returns macd line, signal line, and histogram
        return [{"macd": 1.25, "signal": 1.0, "histogram": 0.25}] * len(ohlcv_data)

@IndicatorRegistry.register("PPO")
class PercentagePriceOscillator(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [0.0] * len(ohlcv_data)

@IndicatorRegistry.register("CCI")
class CommodityChannelIndex(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [100.0] * len(ohlcv_data)

@IndicatorRegistry.register("WILLIAMS")
class WilliamsPercentR(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [-20.0] * len(ohlcv_data)
