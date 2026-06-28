from app.modules.technical.indicators import TechnicalIndicator, IndicatorRegistry

@IndicatorRegistry.register("OBV")
class OnBalanceVolume(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [0.0] * len(ohlcv_data)

@IndicatorRegistry.register("CMF")
class ChaikinMoneyFlow(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [0.0] * len(ohlcv_data)

@IndicatorRegistry.register("MFI")
class MoneyFlowIndex(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[float]:
        return [50.0] * len(ohlcv_data)

@IndicatorRegistry.register("VOLUME_PROFILE")
class VolumeProfile(TechnicalIndicator):
    def calculate(self, ohlcv_data: list[dict]) -> list[dict[str, float]]:
        # Returns value area and volume profile nodes
        return [{"price": 180.0, "volume": 50000.0}] * len(ohlcv_data)
