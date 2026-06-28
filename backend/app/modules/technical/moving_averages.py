from app.modules.technical.indicators import TechnicalIndicator, IndicatorRegistry

@IndicatorRegistry.register("SMA")
class SimpleMovingAverage(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        # SMA formula stub
        period = self.params.get("period", 14)
        return [0.0] * len(ohlcv_data)

@IndicatorRegistry.register("EMA")
class ExponentialMovingAverage(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        # EMA formula stub
        period = self.params.get("period", 14)
        return [0.0] * len(ohlcv_data)

@IndicatorRegistry.register("WMA")
class WeightedMovingAverage(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [0.0] * len(ohlcv_data)

@IndicatorRegistry.register("HMA")
class HullMovingAverage(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [0.0] * len(ohlcv_data)

@IndicatorRegistry.register("VWAP")
class VolumeWeightedAveragePrice(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        # Requires high, low, close, and volume
        return [0.0] * len(ohlcv_data)
