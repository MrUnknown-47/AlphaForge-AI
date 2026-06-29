"""add_backtesting_simulation_tables

Revision ID: ffcff15b8e23
Revises: 890d9bf4df53
Create Date: 2026-06-28 23:12:41.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ffcff15b8e23'
down_revision: Union[str, Sequence[str], None] = '890d9bf4df53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS backtest")

    # Create backtest tables
    op.execute("""
        CREATE TABLE IF NOT EXISTS backtest.strategies (
            id UUID PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(255),
            parameters JSON,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS backtest.runs (
            id UUID PRIMARY KEY,
            strategy_id UUID NOT NULL,
            status VARCHAR(32) DEFAULT 'PENDING',
            started_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP WITH TIME ZONE
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS backtest.orders (
            id UUID PRIMARY KEY,
            run_id UUID NOT NULL,
            symbol VARCHAR(16) NOT NULL,
            qty NUMERIC(20, 8) NOT NULL,
            side VARCHAR(16) NOT NULL,
            order_type VARCHAR(32) DEFAULT 'MARKET',
            status VARCHAR(32) DEFAULT 'FILLED',
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS backtest.trades (
            id UUID PRIMARY KEY,
            run_id UUID NOT NULL,
            symbol VARCHAR(16) NOT NULL,
            price NUMERIC(20, 8) NOT NULL,
            qty NUMERIC(20, 8) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS backtest.positions (
            id UUID PRIMARY KEY,
            run_id UUID NOT NULL,
            symbol VARCHAR(16) NOT NULL,
            qty NUMERIC(20, 8) NOT NULL,
            avg_price NUMERIC(20, 8) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS backtest.snapshots (
            id UUID PRIMARY KEY,
            run_id UUID NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            equity NUMERIC(20, 8) NOT NULL,
            cash NUMERIC(20, 8) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS backtest.metrics (
            id UUID PRIMARY KEY,
            run_id UUID UNIQUE NOT NULL,
            sharpe NUMERIC(10, 4),
            sortino NUMERIC(10, 4),
            calmar NUMERIC(10, 4),
            max_drawdown NUMERIC(10, 4),
            win_rate NUMERIC(10, 4),
            profit_factor NUMERIC(10, 4)
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS backtest.optimizations (
            id UUID PRIMARY KEY,
            strategy_id UUID NOT NULL,
            best_parameters JSON,
            metric_name VARCHAR(50) NOT NULL,
            metric_value NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS backtest.walkforward (
            id UUID PRIMARY KEY,
            strategy_id UUID NOT NULL,
            train_start TIMESTAMP WITH TIME ZONE NOT NULL,
            train_end TIMESTAMP WITH TIME ZONE NOT NULL,
            val_start TIMESTAMP WITH TIME ZONE NOT NULL,
            val_end TIMESTAMP WITH TIME ZONE NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS backtest.montecarlo (
            id UUID PRIMARY KEY,
            run_id UUID NOT NULL,
            simulation_paths INTEGER DEFAULT 1000,
            ruin_probability NUMERIC(10, 4) NOT NULL
        )
    """)

def downgrade() -> None:
    op.drop_table('montecarlo', schema='backtest')
    op.drop_table('walkforward', schema='backtest')
    op.drop_table('optimizations', schema='backtest')
    op.drop_table('metrics', schema='backtest')
    op.drop_table('snapshots', schema='backtest')
    op.drop_table('positions', schema='backtest')
    op.drop_table('trades', schema='backtest')
    op.drop_table('orders', schema='backtest')
    op.drop_table('runs', schema='backtest')
    op.drop_table('strategies', schema='backtest')
