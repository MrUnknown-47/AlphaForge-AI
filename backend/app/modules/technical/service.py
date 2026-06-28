from datetime import datetime
from app.modules.technical.repository import TechnicalRepository
from app.modules.technical.indicators import IndicatorFactory
from app.modules.technical.models import IndicatorsCacheModel
from app.modules.market_data.facade import MarketDataFacade
from app.shared.cache import cache_manager

# Ensure indicators register themselves on load
from app.modules.technical import moving_averages, momentum, volatility, volume, trend, oscillators

class TechnicalService:
    def __init__(self, repo: TechnicalRepository, market_facade: MarketDataFacade):
        self.repo = repo
        self.market_facade = market_facade

    async def calculate_indicator(self, ticker: str, name: str, parameters: dict) -> list:
        # Load last 200 data periods from MarketDataFacade
        end_time = datetime.utcnow()
        # Querying an arbitrary large history interval (e.g. last 30 days) to get enough ticks
        # In a real environment, we'd adjust start/end based on indicator bounds
        start_time = datetime.utcnow() - timedelta(days=30)
        
        ohlcv_bars = await self.market_facade.get_historical_ohlcv(ticker, start_time, end_time)
        
        # Map Pydantic schemas to standard dictionaries for calculations
        mapped_data = [
            {
                "open": float(bar.open),
                "high": float(bar.high),
                "low": float(bar.low),
                "close": float(bar.close),
                "volume": float(bar.volume)
            }
            for bar in ohlcv_bars
        ]

        indicator = IndicatorFactory.create(name, parameters)
        return indicator.calculate(mapped_data)

    async def fetch_cached_indicators(self, ticker: str) -> IndicatorsCacheModel | None:
        # Check Redis cache first
        cache_key = f"tech:indicators:{ticker}:latest"
        cached = await cache_manager.get_json(cache_key)
        if cached:
            return IndicatorsCacheModel(**cached)

        # Fallback to TimescaleDB cache
        model = await self.repo.get_latest_indicators(ticker)
        if model:
            # Update Redis cache (TTL: 1 hour)
            await cache_manager.set_json(cache_key, model.__dict__, ttl=3600)
        return model

# Import timedelta inside service to prevent errors
from datetime import timedelta