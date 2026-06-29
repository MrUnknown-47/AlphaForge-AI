import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, Boolean, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class MlModel(Base):
    __tablename__ = "models"
    __table_args__ = {"schema": "ml"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    version: Mapped[str] = mapped_column(String(20), default="1.0.0")
    status: Mapped[str] = mapped_column(String(20), default="ACTIVE")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class MlTrainingRunModel(Base):
    __tablename__ = "training_runs"
    __table_args__ = {"schema": "ml"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    model_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="COMPLETED")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class MlPredictionModel(Base):
    __tablename__ = "predictions"
    __table_args__ = {"schema": "ml"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    model_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    predicted_return: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    confidence: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class MlMetricsModel(Base):
    __tablename__ = "metrics"
    __table_args__ = {"schema": "ml"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    accuracy: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    mae: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

class MlDriftModel(Base):
    __tablename__ = "drift"
    __table_args__ = {"schema": "ml"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    feature_name: Mapped[str] = mapped_column(String(100), nullable=False)
    psi_value: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    drift_detected: Mapped[bool] = mapped_column(Boolean, default=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class MlFeatureModel(Base):
    __tablename__ = "features"
    __table_args__ = {"schema": "ml"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    data: Mapped[dict] = mapped_column(JSON, default=dict)

class MlForecastModel(Base):
    __tablename__ = "forecasts"
    __table_args__ = {"schema": "ml"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    forecast_type: Mapped[str] = mapped_column(String(50), nullable=False) # e.g. VOLATILITY, DRAWDOWN
    forecast_value: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class MlExplanationModel(Base):
    __tablename__ = "explanations"
    __table_args__ = {"schema": "ml"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    prediction_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    explanation: Mapped[str] = mapped_column(String(1000), nullable=False)

class MlRegistryModel(Base):
    __tablename__ = "registry"
    __table_args__ = {"schema": "ml"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    model_name: Mapped[str] = mapped_column(String(100), nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
