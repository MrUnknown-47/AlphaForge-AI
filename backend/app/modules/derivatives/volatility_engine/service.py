import json
import os
from typing import Dict, Any, List

class VolatilityService:
    @staticmethod
    def generate_volatility_surface(S: float = 100.0) -> Dict[str, Any]:
        strikes = [80.0, 90.0, 95.0, 100.0, 105.0, 110.0, 120.0]
        expiries_days = [30, 60, 90, 180, 360]
        
        surface = []
        for t in expiries_days:
            row = []
            t_years = t / 365.0
            # Term structure effect
            base_vol = 0.25 - 0.05 * (t_years ** 0.5)
            for k in strikes:
                # Volatility smile effect: skew is higher for OTM/ITM options
                moneyness = k / S
                skew = 0.5 * (moneyness - 1.0) ** 2 - 0.1 * (moneyness - 1.0)
                vol = base_vol + skew
                row.append(max(0.05, float(vol)))
            surface.append(row)

        data = {
            "underlying_price": S,
            "strikes": strikes,
            "expiries_days": expiries_days,
            "surface": surface
        }

        # Write to JSON file
        file_dir = os.path.dirname(__file__)
        with open(os.path.join(file_dir, "volatility_surface.json"), "w") as f:
            json.dump(data, f, indent=4)

        return data

    @staticmethod
    def get_volatility_skew(S: float = 100.0) -> List[Dict[str, float]]:
        surface_data = VolatilityService.generate_volatility_surface(S)
        strikes = surface_data["strikes"]
        vols = surface_data["surface"][0] # 30 days
        return [{"strike": strikes[i], "volatility": vols[i]} for i in range(len(strikes))]
class VolatilityEngine:
    pass
