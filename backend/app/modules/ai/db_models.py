import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, Boolean, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class AiAgentModel(Base):
    __tablename__ = "agents"
    __table_args__ = {"schema": "ai"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="ACTIVE")

class AiDebateModel(Base):
    __tablename__ = "debates"
    __table_args__ = {"schema": "ai"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    bull_thesis: Mapped[str] = mapped_column(String(1000), nullable=False)
    bear_thesis: Mapped[str] = mapped_column(String(1000), nullable=False)
    consensus_score: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class AiDecisionModel(Base):
    __tablename__ = "decisions"
    __table_args__ = {"schema": "ai"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    decision_type: Mapped[str] = mapped_column(String(50), nullable=False) # e.g. BUY, SELL
    rationale: Mapped[str] = mapped_column(String(1000), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class AiMemoryModel(Base):
    __tablename__ = "memory"
    __table_args__ = {"schema": "ai"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    key: Mapped[str] = mapped_column(String(100), nullable=False)
    value: Mapped[str] = mapped_column(String(1000), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class AiEmbeddingModel(Base):
    __tablename__ = "embeddings"
    __table_args__ = {"schema": "ai"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    text_content: Mapped[str] = mapped_column(String(2000), nullable=False)
    vector_data: Mapped[dict] = mapped_column(JSON, nullable=False)

class AiExplanationModel(Base):
    __tablename__ = "explanations"
    __table_args__ = {"schema": "ai"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    target: Mapped[str] = mapped_column(String(100), nullable=False)
    explanation: Mapped[str] = mapped_column(String(2000), nullable=False)

class AiReportModel(Base):
    __tablename__ = "reports"
    __table_args__ = {"schema": "ai"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(2000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class AiCommitteeModel(Base):
    __tablename__ = "committees"
    __table_args__ = {"schema": "ai"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    decision: Mapped[str] = mapped_column(String(50), nullable=False) # e.g. HEDGE, REDUCE
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class AiRecommendationModel(Base):
    __tablename__ = "recommendations"
    __table_args__ = {"schema": "ai"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    action: Mapped[str] = mapped_column(String(16), nullable=False)
    reasoning: Mapped[str] = mapped_column(String(500), nullable=False)
