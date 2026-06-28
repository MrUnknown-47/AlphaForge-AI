import uuid
from datetime import datetime, date
from pydantic import BaseModel, Field
from decimal import Decimal

class FinancialStatementCreate(BaseModel):
    ticker: str = Field(..., max_length=16)
    fiscal_period: str = Field(..., max_length=8) # Q1, Q2, FY
    fiscal_year: int = Field(..., gt=1900)
    filing_date: date
    
    total_revenue: Decimal | None = None
    net_income: Decimal | None = None
    eps: Decimal | None = None
    free_cash_flow: Decimal | None = None
    total_debt: Decimal | None = None
    ebitda: Decimal | None = None
    
    roe: Decimal | None = None
    roa: Decimal | None = None
    pe_ratio: Decimal | None = None
    pb_ratio: Decimal | None = None
    market_cap: Decimal | None = None
    shares_outstanding: Decimal | None = None

class FinancialStatementResponse(BaseModel):
    id: uuid.UUID
    ticker: str
    fiscal_period: str
    fiscal_year: int
    filing_date: date
    
    total_revenue: Decimal | None
    net_income: Decimal | None
    eps: Decimal | None
    free_cash_flow: Decimal | None
    total_debt: Decimal | None
    ebitda: Decimal | None
    
    roe: Decimal | None
    roa: Decimal | None
    pe_ratio: Decimal | None
    pb_ratio: Decimal | None
    market_cap: Decimal | None
    shares_outstanding: Decimal | None
    
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True