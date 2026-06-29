"""add_compliance_governance_tables

Revision ID: 5a64a54bed80
Revises: 9682127da88c
Create Date: 2026-06-28 23:49:41.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '5a64a54bed80'
down_revision: Union[str, Sequence[str], None] = '9682127da88c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS compliance")

    # Create compliance tables
    op.execute("""
        CREATE TABLE IF NOT EXISTS compliance.audit_logs (
            id UUID PRIMARY KEY,
            action VARCHAR(100) NOT NULL,
            actor_id VARCHAR(50) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            hash VARCHAR(64) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS compliance.events (
            id UUID PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS compliance.approvals (
            id UUID PRIMARY KEY,
            requested_by VARCHAR(50) NOT NULL,
            approved_by VARCHAR(50),
            status VARCHAR(20) DEFAULT 'PENDING'
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS compliance.policies (
            id UUID PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            rule_definition VARCHAR(500) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS compliance.controls (
            id UUID PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            status VARCHAR(20) DEFAULT 'ACTIVE'
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS compliance.attestations (
            id UUID PRIMARY KEY,
            user_id VARCHAR(50) NOT NULL,
            signed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS compliance.permissions (
            id UUID PRIMARY KEY,
            role VARCHAR(50) NOT NULL,
            resource VARCHAR(50) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS compliance.explanations (
            id UUID PRIMARY KEY,
            decision_id UUID NOT NULL,
            explanation VARCHAR(1000) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS compliance.reports (
            id UUID PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS compliance.retention (
            id UUID PRIMARY KEY,
            record_type VARCHAR(50) NOT NULL,
            retention_period_years INTEGER DEFAULT 7
        )
    """)

def downgrade() -> None:
    op.drop_table('retention', schema='compliance')
    op.drop_table('reports', schema='compliance')
    op.drop_table('explanations', schema='compliance')
    op.drop_table('permissions', schema='compliance')
    op.drop_table('attestations', schema='compliance')
    op.drop_table('controls', schema='compliance')
    op.drop_table('policies', schema='compliance')
    op.drop_table('approvals', schema='compliance')
    op.drop_table('events', schema='compliance')
    op.drop_table('audit_logs', schema='compliance')
