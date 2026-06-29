from typing import Dict, Any, List

class CryptoSpotManager:
    def __init__(self) -> None:
        self.spots = {
            "BTC": {"name": "Bitcoin", "tick_size": 0.01},
            "ETH": {"name": "Ethereum", "tick_size": 0.01},
            "SOL": {"name": "Solana", "tick_size": 0.001},
            "BNB": {"name": "Binance Coin", "tick_size": 0.1},
            "XRP": {"name": "Ripple", "tick_size": 0.0001}
        }

    def get_spot_details(self, symbol: str) -> Dict[str, Any]:
        return self.spots.get(symbol.upper(), {"name": "Generic Crypto Spot", "tick_size": 0.01})
