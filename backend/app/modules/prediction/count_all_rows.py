import os
import psycopg2

def count_rows():
    # Read database URL from env or default config
    db_url = os.environ.get("DATABASE_URL") or "postgresql://postgres:postgres@localhost:5432/alphaforge"
    
    # Clean scheme for psycopg2
    if db_url.startswith("postgresql+psycopg2://"):
        db_url = db_url.replace("postgresql+psycopg2://", "postgresql://")
    elif db_url.startswith("postgresql+asyncpg://"):
        db_url = db_url.replace("postgresql+asyncpg://", "postgresql://")

    print(f"Connecting to database: {db_url}")
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        # 1. Fetch all tables from relevant schemas
        schemas = ('auth', 'market_data', 'fundamental', 'sentiment', 'technical', 'portfolio', 'trading', 'feature_store', 'prediction')
        cur.execute("""
            SELECT table_schema, table_name 
            FROM information_schema.tables 
            WHERE table_schema IN %s
            ORDER BY table_schema, table_name;
        """, (schemas,))
        
        tables = cur.fetchall()
        if not tables:
            print("No tables found in target schemas.")
            return

        print("\n" + "=" * 50)
        print(f"{'SCHEMA.TABLE':<40} | {'ROW COUNT':<10}")
        print("=" * 50)
        
        total_all_rows = 0
        for schema, table_name in tables:
            full_name = f"{schema}.{table_name}"
            try:
                cur.execute(f"SELECT COUNT(*) FROM {full_name};")
                count = cur.fetchone()[0]
                print(f"{full_name:<40} | {count:<10}")
                total_all_rows += count
            except Exception as e:
                print(f"{full_name:<40} | ERROR: {e}")
                
        print("=" * 50)
        print(f"{'TOTAL ROWS ACROSS ALL TABLES':<40} | {total_all_rows:<10}")
        print("=" * 50)

        cur.close()
        conn.close()

    except Exception as e:
        print(f"\n[FATAL] Database connection failed: {e}")
        print("\nPlease ensure your local Postgres database container is running and healthy.")
        print("\nTo count rows manually, you can run this SQL query in your database manager:")
        print("-" * 60)
        print("""
SELECT 
  schemaname, 
  relname as table_name, 
  n_live_tup as row_count 
FROM pg_stat_user_tables 
ORDER BY schemaname, relname;
""")
        print("-" * 60)

if __name__ == "__main__":
    count_rows()
