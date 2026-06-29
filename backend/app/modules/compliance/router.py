from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
from datetime import datetime

from app.shared.database import get_db
from app.modules.compliance.audit import ComplianceAuditLogger
from app.modules.compliance.governance import GovernanceManager
from app.modules.compliance.compliance import ComplianceControlsManager
from app.modules.compliance.surveillance import MarketSurveillance
from app.modules.compliance.explainability import ComplianceExplainer
from app.modules.compliance.policy_engine import CompliancePolicyEngine
from app.modules.compliance.retention import ComplianceRetentionManager
from app.modules.compliance.schemas import (
    AuditLogResponse,
    ComplianceEventResponse,
    CompliancePolicyResponse,
    ComplianceControlResponse,
    ExplainResponse,
    AttestationRequest,
    AttestationResponse,
    CheckRequest,
    CheckResponse
)

router = APIRouter(prefix="/compliance", tags=["Compliance, Audit, Governance & Regulatory"])

audit_logger = ComplianceAuditLogger()
governance_manager = GovernanceManager()
controls_manager = ComplianceControlsManager()
surveillance_engine = MarketSurveillance()
explainer = ComplianceExplainer()
policy_engine = CompliancePolicyEngine()
retention_manager = ComplianceRetentionManager()

@router.get("/audit", response_model=List[AuditLogResponse])
async def get_audit_logs():
    # Immutable audit trail
    log = audit_logger.log_action("risk_override", "PM_01", {"symbol": "TSLA", "override": "drawdown"})
    return [
        {"id": log["id"], "action": log["action"], "actor_id": log["actor_id"], "timestamp": log["timestamp"], "hash": log["hash"]}
    ]

@router.get("/events", response_model=List[ComplianceEventResponse])
async def get_compliance_events():
    return [
        {"id": "EVT_MOCK_1", "name": "RESTRICTED_LIST_CHECK", "timestamp": datetime.utcnow()}
    ]

@router.get("/policies", response_model=List[CompliancePolicyResponse])
async def get_policies():
    return [
        {"id": "POL_MOCK_1", "name": "Pre-Trade Position Limits", "rule_definition": "position_size <= 10000"}
    ]

@router.get("/controls", response_model=List[ComplianceControlResponse])
async def get_controls():
    return [
        {"id": "CTL_MOCK_1", "name": "Restricted Stock Filter", "status": "ACTIVE"}
    ]

@router.get("/permissions")
async def get_permissions(role: str = "TRADER"):
    return {"role": role, "actions_allowed": governance_manager.role_permissions.get(role, [])}

@router.get("/reports")
async def get_regulatory_reports():
    return [
        {"report_name": "SEC Form 13F Quarter Report", "retention_period_years": retention_manager.get_retention_period("audit_records")}
    ]

@router.get("/explanations", response_model=ExplainResponse)
async def get_explanations(decision_id: str = "DEC_MOCK_1"):
    res = explainer.explain_decision(decision_id)
    return res

@router.post("/check", response_model=CheckResponse)
async def check_compliance(req: CheckRequest):
    # Verify Restricted List
    if not controls_manager.verify_symbol(req.symbol):
        return {
            "allowed": False,
            "policy_action": "REJECT",
            "reason": f"Symbol {req.symbol} is on restricted list."
        }
        
    # Evaluate Policies
    res = policy_engine.evaluate_order(req.symbol, req.quantity)
    return res

@router.post("/approve")
async def approve_workflow(requested_by: str, approved_by: str):
    return {"status": "SUCCESS", "message": f"Approval granted by {approved_by} to {requested_by}."}

@router.post("/attest", response_model=AttestationResponse)
async def create_attestation(req: AttestationRequest):
    return {
        "id": "ATTEST_MOCK_1",
        "user_id": req.user_id,
        "signed_at": datetime.utcnow()
    }

@router.post("/escalate")
async def escalate_compliance_breach(breach_id: str):
    return {"status": "SUCCESS", "breach_id": breach_id, "escalation_status": "ESCALATED_TO_CIO"}
