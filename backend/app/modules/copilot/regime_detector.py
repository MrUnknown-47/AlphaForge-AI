from typing import Dict, Any
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.models import CopilotRegimeAnalysis

class RegimeDetector:
    def __init__(self, provider: LLMProvider) -> None:
        self.provider = provider

    async def detect_regime(
        self, vix: float, spy_vol: float, correlations: Dict[str, float]
    ) -> CopilotRegimeAnalysis:
        # High fidelity detection rules based on inputs
        if vix > 30.0 or spy_vol > 0.35:
            vol_state = "HIGH_VOLATILITY"
            regime = "BEAR"
            risk = "RISK_OFF"
        elif vix < 15.0 and spy_vol < 0.15:
            vol_state = "LOW_VOLATILITY"
            regime = "BULL"
            risk = "RISK_ON"
        else:
            vol_state = "NORMAL"
            regime = "SIDEWAYS"
            risk = "RISK_OFF"

        prompt = f"""
        Determine market regime:
        - VIX: {vix}
        - SPY Realized Volatility: {spy_vol:.4f}
        - Asset Correlations: {correlations}
        - Algorithmic regime: {regime}, vol: {vol_state}, risk: {risk}
        
        Refine systemic risk metadata using LLM analysis.
        """
        template = {
            "current_regime": regime,
            "volatility_state": vol_state,
            "systemic_risk": risk
        }
        res = await self.provider.generate_json(prompt, template)
        return CopilotRegimeAnalysis(**res)
