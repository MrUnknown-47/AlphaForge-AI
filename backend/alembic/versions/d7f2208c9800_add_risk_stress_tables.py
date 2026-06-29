"""add_risk_stress_tables

Revision ID: d7f2208c9800
Revises: 4516157a8502
Create Date: 2026-06-28 23:37:41.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd7f2208c9800'
down_revision: Union[str, Sequence[str], None] = '4516157a8502'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS risk")

    # Create risk tables
    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.var (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            var_95 NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.cvar (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            cvar_95 NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.stress (
            id UUID PRIMARY KEY,
            scenario_name VARCHAR(100) NOT NULL,
            expected_loss NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.scenarios (
            id UUID PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(255)
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.exposures (
            id UUID PRIMARY KEY,
            sector VARCHAR(50) NOT NULL,
            exposure_pct NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.drawdowns (
            id UUID PRIMARY KEY,
            max_drawdown NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.correlations (
            id UUID PRIMARY KEY,
            symbol_a VARCHAR(16) NOT NULL,
            symbol_b VARCHAR(16) NOT NULL,
            value NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.contagion (
            id UUID PRIMARY KEY,
            contagion_score NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.liquidity (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            spread_pct NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.limits (
            id UUID PRIMARY KEY,
            limit_type VARCHAR(50) NOT NULL,
            value NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.events (
            id UUID PRIMARY KEY,
            event_type VARCHAR(50) NOT NULL,
            message VARCHAR(255) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk.reports (
            id UUID PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            content VARCHAR(2000) NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

def downgrade() -> None:
    op.drop_table('reports', schema='risk')
    op.drop_table('events', schema='risk')
    op.drop_table('limits', schema='risk')
    op.drop_table('liquidity', schema='risk')
    op.drop_table('contagion', schema='risk')
    op.drop_table('correlations', schema='risk')
    op.drop_table('drawdowns', schema='risk')
    op.drop_table('exposures', schema='risk')
    op.drop_table('scenarios', schema='risk')
    op.drop_table('stress', schema='risk')
    op.drop_table('cvar', schema='risk')
    op.drop_table('var', schema='risk')
