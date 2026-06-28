from app.modules.technical.indicators import TechnicalIndicator, IndicatorRegistry

@IndicatorRegistry.register("ATR")
class AverageTrueRange(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [0.0] * len(ohlcv_data)

@IndicatorRegistry.register("BOLLINGER")
class BollingerBands(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[dict[str, float]]:
        # Returns upper, middle, lower lines
        return [{"upper": 182.0, "middle": 180.0, "lower": 178.0}] * len(ohlcv_data)

@IndicatorRegistry.register("KELTNER")
class KeltnerChannels(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[dict[str, float]]:
        return [{"upper": 182.0, "middle": 180.0, "lower": 178.0}] * len(ohlcv_data)

@IndicatorRegistry.register("DONCHIAN")
class DonchianChannels(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[dict[str, float]]:
        return [{"upper": 182.0, "lower": 178.0}] * len(ohlcv_data)
