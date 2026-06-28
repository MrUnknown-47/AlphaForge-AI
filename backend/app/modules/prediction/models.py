import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.shared.database import Base

class ModelRegistryModel(Base):
    __tablename__ = "model_registry"
    __table_args__ = {"schema": "prediction"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    model_name: Mapped[str] = mapped_column(String(255), nullable=False) # e.g. XGBoost_1d
    version: Mapped[str] = mapped_column(String(64), nullable=False)
    hyperparameters: Mapped[dict] = mapped_column(JSON, nullable=True)
    storage_path: Mapped[str] = mapped_column(String(1024), nullable=True) # MLflow artifact URI
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    metrics: Mapped[list["PredictionMetricsModel"]] = relationship(back_populates="model", cascade="all, delete-orphan")
    explanations: Mapped[list["ExplanationsModel"]] = relationship(back_populates="model", cascade="all, delete-orphan")

class PredictionsModel(Base):
    __tablename__ = "predictions"
    __table_args__ = {"schema": "prediction"}

    time: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    horizon: Mapped[str] = mapped_column(String(8), primary_key=True) # e.g. 1d, 5d, 20d
    
    predicted_value: Mapped[float] = mapped_column(Numeric(12, 6), nullable=False)
    confidence_lower: Mapped[float] = mapped_column(Numeric(12, 6), nullable=False)
    confidence_upper: Mapped[float] = mapped_column(Numeric(12, 6), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class PredictionMetricsModel(Base):
    __tablename__ = "prediction_metrics"
    __table_args__ = {"schema": "prediction"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    model_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("prediction.model_registry.id", ondelete="CASCADE"), nullable=False)
    metric_name: Mapped[str] = mapped_column(String(255), nullable=False) # MSE, MAE, R2
    metric_value: Mapped[float] = mapped_column(Numeric(12, 6), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    model: Mapped["ModelRegistryModel"] = relationship(back_populates="metrics")


class ExplanationsModel(Base):
    __tablename__ = "explanations"
    __table_args__ = {"schema": "prediction"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    model_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("prediction.model_registry.id", ondelete="CASCADE"), nullable=False)
    ticker: Mapped[str] = mapped_column(String(16), nullable=False, index=True)
    
    feature_importances: Mapped[dict] = mapped_column(JSON, nullable=True) # SHAP
    partial_dependence: Mapped[dict] = mapped_column(JSON, nullable=True) # PDP coords
    drift_metrics: Mapped[dict] = mapped_column(JSON, nullable=True) # PSI / KS stats
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    model: Mapped["ModelRegistryModel"] = relationship(back_populates="explanations")