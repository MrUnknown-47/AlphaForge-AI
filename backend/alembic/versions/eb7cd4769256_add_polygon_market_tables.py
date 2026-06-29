"""add_polygon_market_tables

Revision ID: eb7cd4769256
Revises: a88910c7918e
Create Date: 2026-06-28 22:48:11.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'eb7cd4769256'
down_revision: Union[str, Sequence[str], None] = 'a88910c7918e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS market")
    op.execute("CREATE SCHEMA IF NOT EXISTS market_data")

    # Create market schema tables if not exist
    op.execute("""
        CREATE TABLE IF NOT EXISTS market.quotes (
            id UUID PRIMARY KEY,
            ticker VARCHAR(16) NOT NULL,
            bid NUMERIC(20, 8) NOT NULL,
            ask NUMERIC(20, 8) NOT NULL,
            last NUMERIC(20, 8) NOT NULL,
            volume NUMERIC(20, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE NOT NULL
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_market_quotes_ticker ON market.quotes (ticker)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS market.trades (
            id UUID PRIMARY KEY,
            ticker VARCHAR(16) NOT NULL,
            price NUMERIC(20, 8) NOT NULL,
            size NUMERIC(20, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE NOT NULL
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_market_trades_ticker ON market.trades (ticker)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS market.bars (
            id UUID PRIMARY KEY,
            ticker VARCHAR(16) NOT NULL,
            timeframe VARCHAR(16) NOT NULL,
            open NUMERIC(20, 8) NOT NULL,
            high NUMERIC(20, 8) NOT NULL,
            low NUMERIC(20, 8) NOT NULL,
            close NUMERIC(20, 8) NOT NULL,
            volume NUMERIC(20, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE NOT NULL
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_market_bars_ticker ON market.bars (ticker)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS market.options_chain (
            id UUID PRIMARY KEY,
            ticker VARCHAR(16) NOT NULL,
            strike NUMERIC(20, 4) NOT NULL,
            expiration_date DATE NOT NULL,
            option_type VARCHAR(4) NOT NULL,
            bid NUMERIC(20, 8) NOT NULL,
            ask NUMERIC(20, 8) NOT NULL,
            volume INTEGER DEFAULT 0,
            timestamp TIMESTAMP WITH TIME ZONE NOT NULL
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_market_options_chain_ticker ON market.options_chain (ticker)")

    # Create market_data schema tables if not exist
    op.execute("""
        CREATE TABLE IF NOT EXISTS market_data.symbols (
            id UUID PRIMARY KEY,
            ticker VARCHAR(16) UNIQUE NOT NULL,
            name VARCHAR(255) NOT NULL,
            exchange VARCHAR(64) NOT NULL,
            asset_class VARCHAR(64) DEFAULT 'EQUITIES',
            is_active BOOLEAN DEFAULT TRUE
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_market_data_symbols_ticker ON market_data.symbols (ticker)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS market_data.tick_data (
            time TIMESTAMP WITH TIME ZONE NOT NULL,
            ticker VARCHAR(16) NOT NULL,
            price NUMERIC(20, 8) NOT NULL,
            volume NUMERIC(20, 4) NOT NULL,
            bid NUMERIC(20, 8),
            ask NUMERIC(20, 8),
            PRIMARY KEY (time, ticker)
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS market_data.ohlcv_1m (
            time TIMESTAMP WITH TIME ZONE NOT NULL,
            ticker VARCHAR(16) NOT NULL,
            open NUMERIC(20, 8) NOT NULL,
            high NUMERIC(20, 8) NOT NULL,
            low NUMERIC(20, 8) NOT NULL,
            close NUMERIC(20, 8) NOT NULL,
            volume NUMERIC(20, 4) NOT NULL,
            PRIMARY KEY (time, ticker)
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS market_data.ohlcv_5m (
            time TIMESTAMP WITH TIME ZONE NOT NULL,
            ticker VARCHAR(16) NOT NULL,
            open NUMERIC(20, 8) NOT NULL,
            high NUMERIC(20, 8) NOT NULL,
            low NUMERIC(20, 8) NOT NULL,
            close NUMERIC(20, 8) NOT NULL,
            volume NUMERIC(20, 4) NOT NULL,
            PRIMARY KEY (time, ticker)
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS market_data.ohlcv_1h (
            time TIMESTAMP WITH TIME ZONE NOT NULL,
            ticker VARCHAR(16) NOT NULL,
            open NUMERIC(20, 8) NOT NULL,
            high NUMERIC(20, 8) NOT NULL,
            low NUMERIC(20, 8) NOT NULL,
            close NUMERIC(20, 8) NOT NULL,
            volume NUMERIC(20, 4) NOT NULL,
            PRIMARY KEY (time, ticker)
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS market_data.ohlcv_1d (
            time TIMESTAMP WITH TIME ZONE NOT NULL,
            ticker VARCHAR(16) NOT NULL,
            open NUMERIC(20, 8) NOT NULL,
            high NUMERIC(20, 8) NOT NULL,
            low NUMERIC(20, 8) NOT NULL,
            close NUMERIC(20, 8) NOT NULL,
            volume NUMERIC(20, 4) NOT NULL,
            PRIMARY KEY (time, ticker)
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS market_data.corporate_actions (
            id UUID PRIMARY KEY,
            ticker VARCHAR(16) NOT NULL,
            action_type VARCHAR(32) NOT NULL,
            execution_date TIMESTAMP WITH TIME ZONE NOT NULL,
            value NUMERIC(20, 8) NOT NULL
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_market_data_corporate_actions_ticker ON market_data.corporate_actions (ticker)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS market_data.earnings (
            id UUID PRIMARY KEY,
            ticker VARCHAR(16) NOT NULL,
            announcement_date TIMESTAMP WITH TIME ZONE NOT NULL,
            actual_eps NUMERIC(20, 4),
            consensus_eps NUMERIC(20, 4),
            revenue NUMERIC(20, 4)
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_market_data_earnings_ticker ON market_data.earnings (ticker)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS market_data.options_chain (
            time TIMESTAMP WITH TIME ZONE NOT NULL,
            option_symbol VARCHAR(32) NOT NULL,
            ticker VARCHAR(16) NOT NULL,
            strike NUMERIC(20, 4) NOT NULL,
            expiration_date DATE NOT NULL,
            option_type VARCHAR(4) NOT NULL,
            bid NUMERIC(20, 8) NOT NULL,
            ask NUMERIC(20, 8) NOT NULL,
            volume INTEGER DEFAULT 0,
            open_interest INTEGER DEFAULT 0,
            PRIMARY KEY (time, option_symbol)
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_market_data_options_chain_ticker ON market_data.options_chain (ticker)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS market_data.market_calendar (
            id UUID PRIMARY KEY,
            exchange VARCHAR(64) NOT NULL,
            date DATE NOT NULL,
            is_open BOOLEAN DEFAULT TRUE,
            open_time TIMESTAMP WITH TIME ZONE,
            close_time TIMESTAMP WITH TIME ZONE
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_market_data_market_calendar_exchange ON market_data.market_calendar (exchange)")

def downgrade() -> None:
    op.drop_table('bars', schema='market')
    op.drop_table('options_chain', schema='market')
    op.drop_table('quotes', schema='market')
    op.drop_table('trades', schema='market')
