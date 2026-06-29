import numpy as np
from typing import Dict, Any

class ExposureEngine:
    def __init__(self) -> None:
        pass

    def calculate_exposures(self, weights: Dict[str, float], asset_betas: Dict[str, float]) -> Dict[str, float]:
        """Calculates Gross, Net, and Portfolio Beta Exposures."""
        gross = 0.0
        net = 0.0
        portfolio_beta = 0.0
        
        for asset, w in weights.items():
            gross += abs(w)
            net += w
            portfolio_beta += w * asset_betas.get(asset, 1.0)
            
        return {
            "gross_exposure": float(gross),
            "net_exposure": float(net),
            "portfolio_beta": float(portfolio_beta)
        }
