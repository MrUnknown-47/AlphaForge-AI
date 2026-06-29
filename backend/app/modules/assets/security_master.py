import logging
from typing import Dict, Any, List

logger = logging.getLogger("SecurityMaster")

class SecurityMaster:
    def __init__(self) -> None:
        # Standard security specifications store
        self.assets: Dict[str, Dict[str, Any]] = {
            "AAPL": {"type": "EQUITY", "exchange": "NASDAQ", "tick_size": 0.01, "multiplier": 1, "currency": "USD", "margin_requirement": 0.50},
            "AAPL_260717_C150": {"type": "OPTION", "exchange": "OPRA", "tick_size": 0.01, "multiplier": 100, "expiration": "2026-07-17", "currency": "USD", "margin_requirement": 0.20},
            "ES_U26": {"type": "FUTURE", "exchange": "CME", "tick_size": 0.25, "multiplier": 50, "expiration": "2026-09-18", "currency": "USD", "margin_requirement": 0.08},
            "EURUSD": {"type": "FOREX", "exchange": "ICE", "tick_size": 0.0001, "multiplier": 100000, "currency": "USD", "margin_requirement": 0.02},
            "BTCUSD": {"type": "CRYPTO", "exchange": "COINBASE", "tick_size": 0.01, "multiplier": 1, "currency": "USD", "margin_requirement": 0.50},
            "US10Y": {"type": "BOND", "exchange": "CANTOR", "tick_size": 0.0078125, "multiplier": 1000, "currency": "USD", "margin_requirement": 0.01},
            "GLD": {"type": "COMMODITY", "exchange": "NYSE_ARCA", "tick_size": 0.01, "multiplier": 1, "currency": "USD", "margin_requirement": 0.10}
        }

    def get_security_details(self, symbol: str) -> Dict[str, Any]:
        return self.assets.get(symbol, {"type": "EQUITY", "exchange": "NASDAQ", "tick_size": 0.01, "multiplier": 1, "currency": "USD", "margin_requirement": 0.50})

    def add_security(self, symbol: str, details: Dict[str, Any]) -> None:
        self.assets[symbol] = details
        logger.info(f"Registered new multi-asset security: {symbol} [{details.get('type')}]")
