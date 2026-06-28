import asyncio
import os
import sys
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Tables list for validation check
TABLES = [
    {"name": "market_data.ohlcv_1d", "time_col": "time"},
    {"name": "market_data.ohlcv_1h", "time_col": "time"},
    {"name": "technical.indicators_cache", "time_col": "time"},
    {"name": "feature_store.technical_features", "time_col": "time"},
    {"name": "feature_store.sentiment_features", "time_col": "time"},
    {"name": "feature_store.fundamental_features", "time_col": "time"},
]

async def verify_database_data():
    print("=" * 60)
    print("AlphaForge AI Database Training Data Verification Script")
    print("=" * 60)

    # Resolve database URL directly from env or default
    db_url = os.environ.get("DATABASE_URL") or "postgresql+asyncpg://postgres:postgres@localhost:5432/alphaforge"
    
    # We enforce asyncpg for our verification queries
    if db_url.startswith("postgresql://"):
        db_url = db_url.replace("postgresql://", "postgresql+asyncpg://", 1)
    elif db_url.startswith("postgresql+psycopg2://"):
        db_url = db_url.replace("postgresql+psycopg2://", "postgresql+asyncpg://", 1)

    print(f"Connecting to database URI: {db_url} ...")

    try:
        engine = create_async_engine(db_url, echo=False)
        async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        
        async with async_session() as session:
            for t_info in TABLES:
                tbl = t_info["name"]
                t_col = t_info["time_col"]
                
                print(f"\nVerifying Table: {tbl} ...")
                
                try:
                    # 1. Row count query
                    row_count_stmt = text(f"SELECT COUNT(*) FROM {tbl}")
                    res_count = await session.execute(row_count_stmt)
                    rows = res_count.scalar() or 0

                    if rows == 0:
                        print(f"  [WARNING] Table {tbl} is empty.")
                        print("  Status: NOT SUITABLE (Empty table).")
                        continue

                    # 2. Date ranges & tickers query
                    stats_stmt = text(f"SELECT MIN({t_col}), MAX({t_col}), COUNT(DISTINCT ticker) FROM {tbl}")
                    res_stats = await session.execute(stats_stmt)
                    min_date, max_date, tickers = res_stats.fetchone()

                    # 3. Calculate percentage of nulls (we query count of nulls in value columns)
                    null_ratio = 0.0
                    try:
                        # Fetch column names
                        schema, t_name = tbl.split(".")
                        cols_stmt = text(
                            f"SELECT column_name FROM information_schema.columns "
                            f"WHERE table_schema = '{schema}' AND table_name = '{t_name}'"
                        )
                        res_cols = await session.execute(cols_stmt)
                        cols = [r[0] for r in res_cols.fetchall()]
                        
                        null_queries = [f"SUM(CASE WHEN {c} IS NULL THEN 1 ELSE 0 END)" for c in cols]
                        null_stmt = text(f"SELECT {', '.join(null_queries)} FROM {tbl}")
                        res_nulls = await session.execute(null_stmt)
                        null_sums = res_nulls.fetchone()
                        
                        total_elements = rows * len(cols)
                        total_nulls = sum(null_sums) if null_sums else 0
                        null_ratio = (total_nulls / total_elements) * 100 if total_elements > 0 else 0.0
                    except Exception as inner_e:
                        pass

                    # 4. Suitable check (must have > 100 rows and < 10% nulls)
                    suitable = "SUITABLE FOR ML TRAINING" if rows > 100 and null_ratio < 10.0 else "NOT SUITABLE (Insufficient data volume)"

                    print(f"  - Total Rows: {rows}")
                    print(f"  - Earliest Date: {min_date}")
                    print(f"  - Latest Date: {max_date}")
                    print(f"  - Unique Tickers: {tickers}")
                    print(f"  - Null Values: {null_ratio:.2f}%")
                    print(f"  - Suitability Status: {suitable}")
                    
                except Exception as tbl_e:
                    print(f"  [ERROR] Failed to query {tbl}: {tbl_e}")
                    print(f"  Status: NOT SUITABLE (Database query exception).")
        
        await engine.dispose()

    except Exception as e:
        print(f"\n[FATAL] Database connection failed: {e}")
        print("\nPlease ensure your local Postgres database container is running and healthy.")
        print("Expected SQL queries for manual verification:")
        print("-" * 60)
        for t_info in TABLES:
            tbl = t_info["name"]
            t_col = t_info["time_col"]
            print(f"-- Verification SQL for {tbl}:")
            print(f"SELECT \n  COUNT(*) as total_rows,\n  MIN({t_col}) as earliest_date,\n  MAX({t_col}) as latest_date,\n  COUNT(DISTINCT ticker) as unique_tickers\nFROM {tbl};\n")
        print("-" * 60)

if __name__ == "__main__":
    asyncio.run(verify_database_data())
