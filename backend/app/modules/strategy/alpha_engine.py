from typing import Dict, Any
from app.modules.strategy.signal_engine import SignalEngine

class AlphaEngine:
    def __init__(self) -> None:
        self.signal_engine = SignalEngine()

    def generate_alpha_forecasts(self) -> Dict[str, float]:
        """Maps computed signals to direct alpha forecasts (expected returns)."""
        signals = self.signal_engine.compute_signals()
        # raw forecast is signal scaled by 5% expected baseline return
        return {strat: float(sig * 0.05) for strat, sig in signals.items()}
