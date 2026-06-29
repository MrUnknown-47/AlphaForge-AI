"""add_portfolio_sync_tables

Revision ID: 19b92c0f689e
Revises: eb7cd4769256
Create Date: 2026-06-28 22:55:41.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '19b92c0f689e'
down_revision: Union[str, Sequence[str], None] = 'eb7cd4769256'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS portfolio")

    # Create portfolio tables
    op.execute("""
        CREATE TABLE IF NOT EXISTS portfolio.accounts (
            id UUID PRIMARY KEY,
            account_id VARCHAR(100) UNIQUE NOT NULL,
            equity NUMERIC(20, 8) DEFAULT 0.0,
            cash NUMERIC(20, 8) DEFAULT 0.0,
            buying_power NUMERIC(20, 8) DEFAULT 0.0,
            portfolio_value NUMERIC(20, 8) DEFAULT 0.0,
            maintenance_margin NUMERIC(20, 8) DEFAULT 0.0
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS portfolio.positions (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            quantity NUMERIC(20, 8) DEFAULT 0.0,
            avg_price NUMERIC(20, 8) DEFAULT 0.0,
            market_price NUMERIC(20, 8) DEFAULT 0.0,
            market_value NUMERIC(20, 8) DEFAULT 0.0,
            unrealized_pnl NUMERIC(20, 8) DEFAULT 0.0,
            unrealized_pct NUMERIC(10, 4) DEFAULT 0.0
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_portfolio_positions_symbol ON portfolio.positions (symbol)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS portfolio.orders (
            id UUID PRIMARY KEY,
            order_id VARCHAR(100) UNIQUE NOT NULL,
            symbol VARCHAR(16) NOT NULL,
            qty NUMERIC(20, 8) NOT NULL,
            side VARCHAR(16) NOT NULL,
            status VARCHAR(32) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS portfolio.snapshots (
            id UUID PRIMARY KEY,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            equity NUMERIC(20, 8) NOT NULL,
            cash NUMERIC(20, 8) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS portfolio.metrics (
            id UUID PRIMARY KEY,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            sharpe NUMERIC(10, 4),
            sortino NUMERIC(10, 4),
            calmar NUMERIC(10, 4),
            max_drawdown NUMERIC(10, 4),
            volatility NUMERIC(10, 4),
            beta NUMERIC(10, 4),
            alpha NUMERIC(10, 4)
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS portfolio.allocations (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            weight NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS portfolio.risk_metrics (
            id UUID PRIMARY KEY,
            var NUMERIC(20, 8) NOT NULL,
            cvar NUMERIC(20, 8) NOT NULL,
            leverage NUMERIC(10, 4) NOT NULL,
            concentration NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS portfolio.portfolios (
            id UUID PRIMARY KEY,
            user_id UUID NOT NULL,
            name VARCHAR(255) NOT NULL,
            cash_balance NUMERIC(20, 8) DEFAULT 0.0,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_portfolio_portfolios_user_id ON portfolio.portfolios (user_id)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS portfolio.holdings (
            id UUID PRIMARY KEY,
            portfolio_id UUID REFERENCES portfolio.portfolios(id) ON DELETE CASCADE,
            ticker VARCHAR(16) NOT NULL,
            quantity NUMERIC(20, 8) DEFAULT 0.0,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_portfolio_holdings_ticker ON portfolio.holdings (ticker)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS portfolio.transactions (
            id UUID PRIMARY KEY,
            portfolio_id UUID REFERENCES portfolio.portfolios(id) ON DELETE CASCADE,
            transaction_type VARCHAR(16) NOT NULL,
            amount NUMERIC(20, 8) NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

def downgrade() -> None:
    op.drop_table('transactions', schema='portfolio')
    op.drop_table('holdings', schema='portfolio')
    op.drop_table('portfolios', schema='portfolio')
    op.drop_table('risk_metrics', schema='portfolio')
    op.drop_table('allocations', schema='portfolio')
    op.drop_table('metrics', schema='portfolio')
    op.drop_table('snapshots', schema='portfolio')
    op.drop_table('orders', schema='portfolio')
    op.drop_table('positions', schema='portfolio')
    op.drop_table('accounts', schema='portfolio')
