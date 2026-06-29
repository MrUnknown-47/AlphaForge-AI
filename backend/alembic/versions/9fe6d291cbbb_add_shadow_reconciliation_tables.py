"""add_shadow_reconciliation_tables

Revision ID: 9fe6d291cbbb
Revises: 5a64a54bed80
Create Date: 2026-06-28 23:54:41.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9fe6d291cbbb'
down_revision: Union[str, Sequence[str], None] = '5a64a54bed80'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS shadow")

    # Create shadow tables
    op.execute("""
        CREATE TABLE IF NOT EXISTS shadow.runs (
            id UUID PRIMARY KEY,
            status VARCHAR(20) DEFAULT 'ACTIVE',
            started_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS shadow.reconciliations (
            id UUID PRIMARY KEY,
            run_id UUID NOT NULL,
            status VARCHAR(20) DEFAULT 'MATCH',
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS shadow.execution_qualities (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            vwap_slippage_bps NUMERIC(10, 4) DEFAULT 0.0,
            latency_ms NUMERIC(10, 4) DEFAULT 0.0
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS shadow.attributions (
            id UUID PRIMARY KEY,
            sharpe NUMERIC(10, 4) DEFAULT 0.0,
            max_drawdown NUMERIC(10, 4) DEFAULT 0.0
        )
    """)

def downgrade() -> None:
    op.drop_table('attributions', schema='shadow')
    op.drop_table('execution_qualities', schema='shadow')
    op.drop_table('reconciliations', schema='shadow')
    op.drop_table('runs', schema='shadow')
