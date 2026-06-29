import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, Boolean, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class ComplianceAuditLog(Base):
    __tablename__ = "audit_logs"
    __table_args__ = {"schema": "compliance"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    action: Mapped[str] = mapped_column(String(100), nullable=False) # e.g. risk override
    actor_id: Mapped[str] = mapped_column(String(50), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    hash: Mapped[str] = mapped_column(String(64), nullable=False)

class ComplianceEvent(Base):
    __tablename__ = "events"
    __table_args__ = {"schema": "compliance"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ComplianceApproval(Base):
    __tablename__ = "approvals"
    __table_args__ = {"schema": "compliance"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    requested_by: Mapped[str] = mapped_column(String(50), nullable=False)
    approved_by: Mapped[str] = mapped_column(String(50), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="PENDING")

class CompliancePolicy(Base):
    __tablename__ = "policies"
    __table_args__ = {"schema": "compliance"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    rule_definition: Mapped[str] = mapped_column(String(500), nullable=False)

class ComplianceControl(Base):
    __tablename__ = "controls"
    __table_args__ = {"schema": "compliance"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="ACTIVE")

class ComplianceAttestation(Base):
    __tablename__ = "attestations"
    __table_args__ = {"schema": "compliance"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(String(50), nullable=False)
    signed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class CompliancePermission(Base):
    __tablename__ = "permissions"
    __table_args__ = {"schema": "compliance"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    role: Mapped[str] = mapped_column(String(50), nullable=False) # e.g. RISK_MANAGER
    resource: Mapped[str] = mapped_column(String(50), nullable=False)

class ComplianceExplanation(Base):
    __tablename__ = "explanations"
    __table_args__ = {"schema": "compliance"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    decision_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    explanation: Mapped[str] = mapped_column(String(1000), nullable=False)

class ComplianceReport(Base):
    __tablename__ = "reports"
    __table_args__ = {"schema": "compliance"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ComplianceRetention(Base):
    __tablename__ = "retention"
    __table_args__ = {"schema": "compliance"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    record_type: Mapped[str] = mapped_column(String(50), nullable=False) # e.g. executions
    retention_period_years: Mapped[int] = mapped_column(Integer, default=7)
