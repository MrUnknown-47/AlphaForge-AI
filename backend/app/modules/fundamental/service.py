import logging
from app.modules.fundamental.repository import FundamentalRepository
from app.modules.fundamental.providers import FinancialModelingPrepProvider
from app.modules.fundamental.models import FinancialStatementModel
from app.shared.cache import cache_manager

logger = logging.getLogger(__name__)

class FundamentalService:
    def __init__(self, repo: FundamentalRepository) -> None:
        self.repo = repo
        self.provider = FinancialModelingPrepProvider()

    async def get_statements(self, ticker: str, limit: int = 20) -> list[FinancialStatementModel]:
        return await self.repo.get_financial_statements(ticker, limit)

    async def sync_ticker_fundamentals(self, ticker: str, limit: int = 20) -> None:
        logger.info(f"Initiating quarterly fundamentals sync for {ticker}...")
        
        # 1. Download from FinancialModelingPrep
        statements = await self.provider.get_quarterly_statements(ticker, limit)
        if not statements:
            logger.warning(f"No statement data returned from FMP provider for {ticker}.")
            return

        # 2. Write batch to TimescaleDB
        await self.repo.insert_financial_statements_batch(statements)

        # 3. Cache the latest ratios inside Redis (using hash structure for online lookups)
        latest = statements[0]
        cache_key = f"fundamental:ratios:{ticker}"
        ratios_payload = {
            "pe_ratio": float(latest["pe_ratio"]) if latest.get("pe_ratio") else 0.0,
            "pb_ratio": float(latest["pb_ratio"]) if latest.get("pb_ratio") else 0.0,
            "roe": float(latest["roe"]) if latest.get("roe") else 0.0,
            "debt_to_equity": float(latest["total_debt"]) / (float(latest["market_cap"]) / float(latest["pb_ratio"])) if (latest.get("market_cap") and latest.get("pb_ratio") and float(latest["pb_ratio"]) > 0) else 0.45,
            "timestamp": latest["filing_date"].isoformat()
        }
        await cache_manager.set_json(cache_key, ratios_payload, ttl=86400) # Cache for 24 hours
        logger.info(f"Fundamentals sync complete for {ticker}. Cached ratios in Redis.")

    async def run_backfill_all_symbols(self) -> None:
        """Triggers historical backfills for the core quantitative platform symbols."""
        tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "AMD", "SPY", "QQQ"]
        for ticker in tickers:
            try:
                # Backfill last 20 quarters (5 years)
                await self.sync_ticker_fundamentals(ticker, limit=20)
            except Exception as e:
                logger.error(f"Error during backfilling fundamentals for {ticker}: {e}")