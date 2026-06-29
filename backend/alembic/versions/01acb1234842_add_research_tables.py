"""add_research_tables

Revision ID: 01acb1234842
Revises: ffcff15b8e23
Create Date: 2026-06-28 23:18:41.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '01acb1234842'
down_revision: Union[str, Sequence[str], None] = 'ffcff15b8e23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS research")

    # Create research tables
    op.execute("""
        CREATE TABLE IF NOT EXISTS research.factors (
            id UUID PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            description VARCHAR(255),
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS research.features (
            id UUID PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            feature_type VARCHAR(50) NOT NULL,
            data JSON
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS research.factor_exposures (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            momentum NUMERIC(10, 4) DEFAULT 0.0,
            value_factor NUMERIC(10, 4) DEFAULT 0.0,
            growth NUMERIC(10, 4) DEFAULT 0.0,
            quality NUMERIC(10, 4) DEFAULT 0.0,
            volatility NUMERIC(10, 4) DEFAULT 0.0,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS research.validations (
            id UUID PRIMARY KEY,
            metric_name VARCHAR(50) NOT NULL,
            p_value NUMERIC(10, 4) NOT NULL,
            passed BOOLEAN DEFAULT TRUE,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS research.regimes (
            id UUID PRIMARY KEY,
            regime_name VARCHAR(50) NOT NULL,
            probability NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS research.correlations (
            id UUID PRIMARY KEY,
            symbol_a VARCHAR(16) NOT NULL,
            symbol_b VARCHAR(16) NOT NULL,
            correlation_value NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS research.clusters (
            id UUID PRIMARY KEY,
            cluster_id INTEGER NOT NULL,
            symbol VARCHAR(16) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS research.explanations (
            id UUID PRIMARY KEY,
            feature_name VARCHAR(100) NOT NULL,
            shap_value NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS research.optimizations (
            id UUID PRIMARY KEY,
            metric_name VARCHAR(50) NOT NULL,
            metric_value NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS research.reports (
            id UUID PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            content VARCHAR(2000) NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

def downgrade() -> None:
    op.drop_table('reports', schema='research')
    op.drop_table('optimizations', schema='research')
    op.drop_table('explanations', schema='research')
    op.drop_table('clusters', schema='research')
    op.drop_table('correlations', schema='research')
    op.drop_table('regimes', schema='research')
    op.drop_table('validations', schema='research')
    op.drop_table('factor_exposures', schema='research')
    op.drop_table('features', schema='research')
    op.drop_table('factors', schema='research')
