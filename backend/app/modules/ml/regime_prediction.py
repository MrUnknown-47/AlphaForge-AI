from typing import List, Dict, Any

class RegimePredictor:
    def predict_regime(self, prices: List[float]) -> Dict[str, Any]:
        if not prices:
            return {"regime": "SIDEWAYS", "probability": 1.0}
            
        ret = (prices[-1] - prices[0]) / prices[0] if len(prices) > 1 else 0.0
        
        if ret > 0.05:
            regime = "BULL"
        elif ret < -0.05:
            regime = "BEAR"
        else:
            regime = "SIDEWAYS"
            
        return {
            "regime": regime,
            "probability": 0.82
        }
