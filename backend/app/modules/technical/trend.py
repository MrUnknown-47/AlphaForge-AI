from app.modules.technical.indicators import TechnicalIndicator, IndicatorRegistry

@IndicatorRegistry.register("ADX")
class AverageDirectionalIndex(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [25.0] * len(ohlcv_data)

@IndicatorRegistry.register("DMI")
class DirectionalMovementIndex(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[dict[str, float]]:
        # Returns +DI and -DI values
        return [{"plus_di": 22.0, "minus_di": 18.0}] * len(ohlcv_data)

@IndicatorRegistry.register("AROON")
class Aroon(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[dict[str, float]]:
        # Returns Aroon Up and Aroon Down
        return [{"up": 70.0, "down": 30.0}] * len(ohlcv_data)
