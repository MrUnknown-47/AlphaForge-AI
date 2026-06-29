from pydantic import BaseModel
from typing import Dict, Any, Optional

class AssetSpecsResponse(BaseModel):
    symbol: str
    asset_type: str
    exchange: str
    tick_size: float
    multiplier: float
    currency: str
    margin_requirement: float
