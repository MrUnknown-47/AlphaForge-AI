from pydantic import BaseModel
from typing import Dict, Any, List

class FundMetricsResponse(BaseModel):
    nav: float
    aum: float
    leverage: float
    fees: Dict[str, float]
    hurdle_rate: float
