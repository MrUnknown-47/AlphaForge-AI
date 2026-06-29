import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, Boolean, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class ShadowRunModel(Base):
    __tablename__ = "runs"
    __table_args__ = {"schema": "shadow"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    status: Mapped[str] = mapped_column(String(20), default="ACTIVE")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ShadowReconciliationModel(Base):
    __tablename__ = "reconciliations"
    __table_args__ = {"schema": "shadow"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="MATCH") # MATCH, WARNING, BREAK
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ShadowExecutionQualityModel(Base):
    __tablename__ = "execution_qualities"
    __table_args__ = {"schema": "shadow"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    vwap_slippage_bps: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)
    latency_ms: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)

class ShadowAttributionModel(Base):
    __tablename__ = "attributions"
    __table_args__ = {"schema": "shadow"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    sharpe: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)
    max_drawdown: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)
