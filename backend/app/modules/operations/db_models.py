import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, Boolean, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class OpsMetricsModel(Base):
    __tablename__ = "metrics"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    value: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class OpsLogsModel(Base):
    __tablename__ = "logs"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    message: Mapped[str] = mapped_column(String(500), nullable=False)
    level: Mapped[str] = mapped_column(String(20), default="INFO")
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class OpsAlertsModel(Base):
    __tablename__ = "alerts"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    alert_type: Mapped[str] = mapped_column(String(50), nullable=False)
    message: Mapped[str] = mapped_column(String(255), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class OpsIncidentsModel(Base):
    __tablename__ = "incidents"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    severity: Mapped[str] = mapped_column(String(20), nullable=False) # e.g. CRITICAL
    message: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="ACTIVE")
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class OpsTelemetryModel(Base):
    __tablename__ = "telemetry"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    cpu_pct: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    memory_pct: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    api_latency_ms: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class OpsTracesModel(Base):
    __tablename__ = "traces"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    span_id: Mapped[str] = mapped_column(String(100), nullable=False)
    duration_ms: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

class OpsHealthModel(Base):
    __tablename__ = "health"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    status: Mapped[str] = mapped_column(String(20), nullable=False) # e.g. GREEN, RED
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class OpsEventsModel(Base):
    __tablename__ = "events"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_name: Mapped[str] = mapped_column(String(50), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class OpsServicesModel(Base):
    __tablename__ = "services"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    service_name: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="ACTIVE")

class OpsReportsModel(Base):
    __tablename__ = "reports"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(2000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
class NOCModel(Base):
    __tablename__ = "noc"
    __table_args__ = {"schema": "ops"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    service_name: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="GREEN")
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
