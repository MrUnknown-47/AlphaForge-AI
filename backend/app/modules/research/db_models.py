import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, Boolean, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class ResearchFactorModel(Base):
    __tablename__ = "factors"
    __table_args__ = {"schema": "research"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ResearchFeatureModel(Base):
    __tablename__ = "features"
    __table_args__ = {"schema": "research"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    feature_type: Mapped[str] = mapped_column(String(50), nullable=False)
    data: Mapped[dict] = mapped_column(JSON, default=dict)

class ResearchFactorExposureModel(Base):
    __tablename__ = "factor_exposures"
    __table_args__ = {"schema": "research"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    momentum: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)
    value_factor: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)
    growth: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)
    quality: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)
    volatility: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ResearchValidationModel(Base):
    __tablename__ = "validations"
    __table_args__ = {"schema": "research"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    metric_name: Mapped[str] = mapped_column(String(50), nullable=False)
    p_value: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    passed: Mapped[bool] = mapped_column(Boolean, default=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ResearchRegimeModel(Base):
    __tablename__ = "regimes"
    __table_args__ = {"schema": "research"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    regime_name: Mapped[str] = mapped_column(String(50), nullable=False) # e.g. BULL, BEAR
    probability: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ResearchCorrelationModel(Base):
    __tablename__ = "correlations"
    __table_args__ = {"schema": "research"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol_a: Mapped[str] = mapped_column(String(16), nullable=False)
    symbol_b: Mapped[str] = mapped_column(String(16), nullable=False)
    correlation_value: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ResearchClusterModel(Base):
    __tablename__ = "clusters"
    __table_args__ = {"schema": "research"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    cluster_id: Mapped[int] = mapped_column(Integer, nullable=False)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ResearchExplanationModel(Base):
    __tablename__ = "explanations"
    __table_args__ = {"schema": "research"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    feature_name: Mapped[str] = mapped_column(String(100), nullable=False)
    shap_value: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ResearchOptimizationModel(Base):
    __tablename__ = "optimizations"
    __table_args__ = {"schema": "research"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    metric_name: Mapped[str] = mapped_column(String(50), nullable=False)
    metric_value: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ResearchReportModel(Base):
    __tablename__ = "reports"
    __table_args__ = {"schema": "research"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(2000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
