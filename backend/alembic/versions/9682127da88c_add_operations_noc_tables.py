"""add_operations_noc_tables

Revision ID: 9682127da88c
Revises: d7f2208c9800
Create Date: 2026-06-28 23:45:41.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9682127da88c'
down_revision: Union[str, Sequence[str], None] = 'd7f2208c9800'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS ops")

    # Create ops tables
    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.metrics (
            id UUID PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            value NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.logs (
            id UUID PRIMARY KEY,
            message VARCHAR(500) NOT NULL,
            level VARCHAR(20) DEFAULT 'INFO',
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.alerts (
            id UUID PRIMARY KEY,
            alert_type VARCHAR(50) NOT NULL,
            message VARCHAR(255) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.incidents (
            id UUID PRIMARY KEY,
            severity VARCHAR(20) NOT NULL,
            message VARCHAR(255) NOT NULL,
            status VARCHAR(20) DEFAULT 'ACTIVE',
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.telemetry (
            id UUID PRIMARY KEY,
            cpu_pct NUMERIC(10, 4) NOT NULL,
            memory_pct NUMERIC(10, 4) NOT NULL,
            api_latency_ms NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.traces (
            id UUID PRIMARY KEY,
            span_id VARCHAR(100) NOT NULL,
            duration_ms NUMERIC(10, 4) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.health (
            id UUID PRIMARY KEY,
            status VARCHAR(20) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.events (
            id UUID PRIMARY KEY,
            event_name VARCHAR(50) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.services (
            id UUID PRIMARY KEY,
            service_name VARCHAR(100) NOT NULL,
            status VARCHAR(20) DEFAULT 'ACTIVE'
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.reports (
            id UUID PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            content VARCHAR(2000) NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ops.noc (
            id UUID PRIMARY KEY,
            service_name VARCHAR(100) NOT NULL,
            status VARCHAR(20) DEFAULT 'GREEN',
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

def downgrade() -> None:
    op.drop_table('noc', schema='ops')
    op.drop_table('reports', schema='ops')
    op.drop_table('services', schema='ops')
    op.drop_table('events', schema='ops')
    op.drop_table('health', schema='ops')
    op.drop_table('traces', schema='ops')
    op.drop_table('telemetry', schema='ops')
    op.drop_table('incidents', schema='ops')
    op.drop_table('alerts', schema='ops')
    op.drop_table('logs', schema='ops')
    op.drop_table('metrics', schema='ops')
