"""add_live_execution_tables

Revision ID: 890d9bf4df53
Revises: 19b92c0f689e
Create Date: 2026-06-28 23:02:41.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '890d9bf4df53'
down_revision: Union[str, Sequence[str], None] = '19b92c0f689e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS execution")

    # Create execution tables
    op.execute("""
        CREATE TABLE IF NOT EXISTS execution.orders (
            id UUID PRIMARY KEY,
            broker_order_id VARCHAR(100) UNIQUE NOT NULL,
            symbol VARCHAR(16) NOT NULL,
            qty NUMERIC(20, 8) NOT NULL,
            side VARCHAR(16) NOT NULL,
            status VARCHAR(32) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS execution.fills (
            id UUID PRIMARY KEY,
            broker_order_id VARCHAR(100) NOT NULL,
            symbol VARCHAR(16) NOT NULL,
            price NUMERIC(20, 8) NOT NULL,
            qty NUMERIC(20, 8) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS execution.positions (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) UNIQUE NOT NULL,
            qty NUMERIC(20, 8) NOT NULL,
            entry_price NUMERIC(20, 8) NOT NULL,
            current_price NUMERIC(20, 8) NOT NULL,
            unrealized_pnl NUMERIC(20, 8) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS execution.telemetry (
            id UUID PRIMARY KEY,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            symbol VARCHAR(16) NOT NULL,
            side VARCHAR(16) NOT NULL,
            quantity NUMERIC(20, 8) NOT NULL,
            requested_price NUMERIC(20, 8) NOT NULL,
            executed_price NUMERIC(20, 8) NOT NULL,
            slippage NUMERIC(20, 8) NOT NULL,
            commission NUMERIC(10, 4) DEFAULT 0.0,
            latency NUMERIC(10, 4) NOT NULL,
            broker_order_id VARCHAR(100) NOT NULL,
            strategy_id VARCHAR(100)
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS execution.pnl (
            id UUID PRIMARY KEY,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            realized_pnl NUMERIC(20, 8) NOT NULL,
            unrealized_pnl NUMERIC(20, 8) NOT NULL,
            daily_pnl NUMERIC(20, 8) NOT NULL,
            portfolio_pnl NUMERIC(20, 8) NOT NULL,
            running_equity NUMERIC(20, 8) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS execution.slippage (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            arrival_price NUMERIC(20, 8) NOT NULL,
            fill_price NUMERIC(20, 8) NOT NULL,
            slippage_bps NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS execution.events (
            id UUID PRIMARY KEY,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            event_type VARCHAR(50) NOT NULL,
            message VARCHAR(255) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS execution.sessions (
            id UUID PRIMARY KEY,
            active BOOLEAN DEFAULT TRUE,
            started_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

def downgrade() -> None:
    op.drop_table('sessions', schema='execution')
    op.drop_table('events', schema='execution')
    op.drop_table('slippage', schema='execution')
    op.drop_table('pnl', schema='execution')
    op.drop_table('telemetry', schema='execution')
    op.drop_table('positions', schema='execution')
    op.drop_table('fills', schema='execution')
    op.drop_table('orders', schema='execution')
