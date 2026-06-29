from typing import Dict, Any, List

class FundRegistry:
    def __init__(self) -> None:
        self.registry = {
            "AF_LONG_SHORT": {"name": "AlphaForge Long Short Fund", "benchmark": "SPY", "leverage_limit": 2.0},
            "AF_GLOBAL_MACRO": {"name": "AlphaForge Global Macro", "benchmark": "ACWI", "leverage_limit": 3.0},
            "AF_CTA": {"name": "AlphaForge CTA Trend Follower", "benchmark": "SG_CTA", "leverage_limit": 5.0},
            "AF_QUANT_EQUITY": {"name": "AlphaForge Quant Equity", "benchmark": "SPY", "leverage_limit": 1.5}
        }

    def get_fund_specs(self, fund_id: str) -> Dict[str, Any]:
        return self.registry.get(fund_id.upper(), {"name": "Generic Hedge Fund", "benchmark": "SPY", "leverage_limit": 2.0})
