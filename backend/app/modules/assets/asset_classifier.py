class AssetClassifier:
    def __init__(self) -> None:
        pass

    def classify(self, asset_type: str) -> str:
        """Classifies asset class types to determine corporate actions, trading desks, or margin bounds."""
        types_map = {
            "EQUITY": "Risk Asset - Stocks",
            "OPTION": "Leveraged Derivatives - Options",
            "FUTURE": "Leveraged Derivatives - Futures",
            "FOREX": "Yield / Carry Asset - Currencies",
            "CRYPTO": "Speculative Asset - Coins",
            "BOND": "Fixed Income Asset - Treasuries",
            "COMMODITY": "Inflation Protective Asset - Hard Assets"
        }
        return types_map.get(asset_type.upper(), "Alternative Assets Class")
