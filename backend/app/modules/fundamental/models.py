import uuid
from datetime import datetime, date
from sqlalchemy import String, Numeric, DateTime, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class FinancialStatementModel(Base):
    __tablename__ = "financial_statements"
    __table_args__ = {"schema": "fundamental"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    ticker: Mapped[str] = mapped_column(String(16), nullable=False, index=True)
    fiscal_period: Mapped[str] = mapped_column(String(8), nullable=False) # e.g. Q1, Q2, FY
    fiscal_year: Mapped[int] = mapped_column(Integer, nullable=False)
    filing_date: Mapped[date] = mapped_column(Date, nullable=False)
    
    total_revenue: Mapped[float] = mapped_column(Numeric(24, 4), nullable=True)
    net_income: Mapped[float] = mapped_column(Numeric(24, 4), nullable=True)
    eps: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    free_cash_flow: Mapped[float] = mapped_column(Numeric(24, 4), nullable=True)
    total_debt: Mapped[float] = mapped_column(Numeric(24, 4), nullable=True)
    ebitda: Mapped[float] = mapped_column(Numeric(24, 4), nullable=True)
    
    roe: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    roa: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    pe_ratio: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    pb_ratio: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    market_cap: Mapped[float] = mapped_column(Numeric(24, 4), nullable=True)
    shares_outstanding: Mapped[float] = mapped_column(Numeric(24, 4), nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)