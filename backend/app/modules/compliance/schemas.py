from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class AuditLogResponse(BaseModel):
    id: str
    action: str
    actor_id: str
    timestamp: datetime
    hash: str

class ComplianceEventResponse(BaseModel):
    id: str
    name: str
    timestamp: datetime

class CompliancePolicyResponse(BaseModel):
    id: str
    name: str
    rule_definition: str

class ComplianceControlResponse(BaseModel):
    id: str
    name: str
    status: str

class ExplainResponse(BaseModel):
    decision_id: str
    explanation: str

class AttestationRequest(BaseModel):
    user_id: str

class AttestationResponse(BaseModel):
    id: str
    user_id: str
    signed_at: datetime

class CheckRequest(BaseModel):
    symbol: str
    action: str # BUY, SELL
    quantity: int
    actor_id: str

class CheckResponse(BaseModel):
    allowed: bool
    policy_action: str # ALLOW, WARN, REJECT, ESCALATE, KILL_SWITCH
    reason: str
