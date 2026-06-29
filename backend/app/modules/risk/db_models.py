import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, Boolean, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class RiskVarModel(Base):
    __tablename__ = "var"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    var_95: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class RiskCvarModel(Base):
    __tablename__ = "cvar"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    cvar_95: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class RiskStressModel(Base):
    __tablename__ = "stress"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    scenario_name: Mapped[str] = mapped_column(String(100), nullable=False)
    expected_loss: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

class RiskScenarioModel(Base):
    __tablename__ = "scenarios"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

class RiskExposureModel(Base):
    __tablename__ = "exposures"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    sector: Mapped[str] = mapped_column(String(50), nullable=False)
    exposure_pct: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

class RiskDrawdownModel(Base):
    __tablename__ = "drawdowns"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    max_drawdown: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class RiskCorrelationModel(Base):
    __tablename__ = "correlations"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol_a: Mapped[str] = mapped_column(String(16), nullable=False)
    symbol_b: Mapped[str] = mapped_column(String(16), nullable=False)
    value: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

class RiskContagionModel(Base):
    __tablename__ = "contagion"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    contagion_score: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

class RiskLiquidityModel(Base):
    __tablename__ = "liquidity"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    spread_pct: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

class RiskLimitModel(Base):
    __tablename__ = "limits"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    limit_type: Mapped[str] = mapped_column(String(50), nullable=False) # e.g. POSITION
    value: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

class RiskEventModel(Base):
    __tablename__ = "events"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_type: Mapped[str] = mapped_column(String(50), nullable=False)
    message: Mapped[str] = mapped_column(String(255), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class RiskReportModel(Base):
    __tablename__ = "reports"
    __table_args__ = {"schema": "risk"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(2000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
