"""add_ml_forecasting_tables

Revision ID: 4516157a8502
Revises: 5443569915e5
Create Date: 2026-06-28 23:32:41.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '4516157a8502'
down_revision: Union[str, Sequence[str], None] = '5443569915e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS ml")

    # Create ml tables
    op.execute("""
        CREATE TABLE IF NOT EXISTS ml.models (
            id UUID PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            version VARCHAR(20) DEFAULT '1.0.0',
            status VARCHAR(20) DEFAULT 'ACTIVE',
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ml.training_runs (
            id UUID PRIMARY KEY,
            model_id UUID NOT NULL,
            status VARCHAR(20) DEFAULT 'COMPLETED',
            started_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ml.predictions (
            id UUID PRIMARY KEY,
            model_id UUID NOT NULL,
            symbol VARCHAR(16) NOT NULL,
            predicted_return NUMERIC(10, 4) NOT NULL,
            confidence NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ml.metrics (
            id UUID PRIMARY KEY,
            run_id UUID NOT NULL,
            accuracy NUMERIC(10, 4) NOT NULL,
            mae NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ml.drift (
            id UUID PRIMARY KEY,
            feature_name VARCHAR(100) NOT NULL,
            psi_value NUMERIC(10, 4) NOT NULL,
            drift_detected BOOLEAN DEFAULT FALSE,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ml.features (
            id UUID PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            data JSON
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ml.forecasts (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            forecast_type VARCHAR(50) NOT NULL,
            forecast_value NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ml.explanations (
            id UUID PRIMARY KEY,
            prediction_id UUID NOT NULL,
            explanation VARCHAR(1000) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ml.registry (
            id UUID PRIMARY KEY,
            model_name VARCHAR(100) NOT NULL,
            registered_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

def downgrade() -> None:
    op.drop_table('registry', schema='ml')
    op.drop_table('explanations', schema='ml')
    op.drop_table('forecasts', schema='ml')
    op.drop_table('features', schema='ml')
    op.drop_table('drift', schema='ml')
    op.drop_table('metrics', schema='ml')
    op.drop_table('predictions', schema='ml')
    op.drop_table('training_runs', schema='ml')
    op.drop_table('models', schema='ml')
