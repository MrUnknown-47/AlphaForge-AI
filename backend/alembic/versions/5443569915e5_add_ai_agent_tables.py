"""add_ai_agent_tables

Revision ID: 5443569915e5
Revises: 01acb1234842
Create Date: 2026-06-28 23:25:41.636156

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '5443569915e5'
down_revision: Union[str, Sequence[str], None] = '01acb1234842'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create schemas if they don't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS ai")

    # Create ai tables
    op.execute("""
        CREATE TABLE IF NOT EXISTS ai.agents (
            id UUID PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            role VARCHAR(50) NOT NULL,
            status VARCHAR(20) DEFAULT 'ACTIVE'
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ai.debates (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            bull_thesis VARCHAR(1000) NOT NULL,
            bear_thesis VARCHAR(1000) NOT NULL,
            consensus_score NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ai.decisions (
            id UUID PRIMARY KEY,
            decision_type VARCHAR(50) NOT NULL,
            rationale VARCHAR(1000) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ai.memory (
            id UUID PRIMARY KEY,
            key VARCHAR(100) NOT NULL,
            value VARCHAR(1000) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ai.embeddings (
            id UUID PRIMARY KEY,
            text_content VARCHAR(2000) NOT NULL,
            vector_data JSON NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ai.explanations (
            id UUID PRIMARY KEY,
            target VARCHAR(100) NOT NULL,
            explanation VARCHAR(2000) NOT NULL
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ai.reports (
            id UUID PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            content VARCHAR(2000) NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ai.committees (
            id UUID PRIMARY KEY,
            decision VARCHAR(50) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ai.recommendations (
            id UUID PRIMARY KEY,
            symbol VARCHAR(16) NOT NULL,
            action VARCHAR(16) NOT NULL,
            reasoning VARCHAR(500) NOT NULL
        )
    """)

def downgrade() -> None:
    op.drop_table('recommendations', schema='ai')
    op.drop_table('committees', schema='ai')
    op.drop_table('reports', schema='ai')
    op.drop_table('explanations', schema='ai')
    op.drop_table('embeddings', schema='ai')
    op.drop_table('memory', schema='ai')
    op.drop_table('decisions', schema='ai')
    op.drop_table('debates', schema='ai')
    op.drop_table('agents', schema='ai')
