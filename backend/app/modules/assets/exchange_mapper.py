class ExchangeMapper:
    def __init__(self) -> None:
        pass

    def get_market_hours(self, exchange: str) -> str:
        """Determines operating hours (EST) for a given global exchange."""
        exch = exchange.upper()
        if exch in ["NYSE", "NASDAQ", "NYSE_ARCA"]:
            return "09:30 - 16:00 EST"
        elif exch in ["CME", "ICE"]:
            return "24 Hours (Sunday 18:00 - Friday 17:00 EST)"
        elif exch in ["OPRA"]:
            return "09:30 - 16:00 EST"
        elif exch in ["COINBASE", "BINANCE"]:
            return "24 Hours / 7 Days / 365 Days"
        return "09:00 - 17:00 Local Time"
