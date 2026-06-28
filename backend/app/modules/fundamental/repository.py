import logging
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.fundamental.models import FinancialStatementModel

logger = logging.getLogger(__name__)

class FundamentalRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_financial_statements(self, ticker: str, limit: int = 20) -> list[FinancialStatementModel]:
        stmt = (
            select(FinancialStatementModel)
            .where(FinancialStatementModel.ticker == ticker)
            .order_by(FinancialStatementModel.fiscal_year.desc(), FinancialStatementModel.fiscal_period.desc())
            .limit(limit)
        )
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def insert_financial_statements_batch(self, statements: list[dict]) -> None:
        if not statements:
            return

        values = [
            {
                "ticker": s["ticker"],
                "fiscal_period": s["fiscal_period"],
                "fiscal_year": s["fiscal_year"],
                "filing_date": s["filing_date"],
                "total_revenue": float(s["total_revenue"]) if s["total_revenue"] else None,
                "net_income": float(s["net_income"]) if s["net_income"] else None,
                "eps": float(s["eps"]) if s["eps"] else None,
                "free_cash_flow": float(s["free_cash_flow"]) if s["free_cash_flow"] else None,
                "total_debt": float(s["total_debt"]) if s["total_debt"] else None,
                "ebitda": float(s["ebitda"]) if s["ebitda"] else None,
                "roe": float(s["roe"]) if s["roe"] else None,
                "roa": float(s["roa"]) if s["roa"] else None,
                "pe_ratio": float(s["pe_ratio"]) if s["pe_ratio"] else None,
                "pb_ratio": float(s["pb_ratio"]) if s["pb_ratio"] else None,
                "market_cap": float(s["market_cap"]) if s["market_cap"] else None,
                "shares_outstanding": float(s["shares_outstanding"]) if s["shares_outstanding"] else None
            }
            for s in statements
        ]

        # Use SQLAlchemy Core bulk insert
        stmt = insert(FinancialStatementModel)
        try:
            await self.db.execute(stmt, values)
            await self.db.commit()
            logger.info(f"Successfully batch-inserted {len(statements)} fundamental statement rows for {statements[0]['ticker']}.")
        except Exception as e:
            await self.db.rollback()
            logger.warning(f"Batch insert for fundamentals failed: {e}. Attempting standard merge loop...")
            
            # Safe database merge loop fallback for SQLite / test environments
            for val in values:
                stmt_select = select(FinancialStatementModel).where(
                    FinancialStatementModel.ticker == val["ticker"],
                    FinancialStatementModel.fiscal_period == val["fiscal_period"],
                    FinancialStatementModel.fiscal_year == val["fiscal_year"]
                )
                res = await self.db.execute(stmt_select)
                existing = res.scalars().first()
                if not existing:
                    new_stmt = FinancialStatementModel(**val)
                    self.db.add(new_stmt)
            await self.db.commit()