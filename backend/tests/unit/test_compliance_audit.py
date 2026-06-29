import pytest
from app.modules.compliance.audit import ComplianceAuditLogger
from app.modules.compliance.governance import GovernanceManager
from app.modules.compliance.compliance import ComplianceControlsManager
from app.modules.compliance.surveillance import MarketSurveillance
from app.modules.compliance.explainability import ComplianceExplainer
from app.modules.compliance.policy_engine import CompliancePolicyEngine
from app.modules.compliance.retention import ComplianceRetentionManager

@pytest.mark.asyncio
async def test_audit_trail_hashes():
    logger = ComplianceAuditLogger()
    
    log1 = logger.log_action("risk_override", "PM_1", {"override": "limits"})
    log2 = logger.log_action("trade_execution", "TRADER_1", {"order": "buy"})
    
    assert log1["hash"] != log2["hash"]
    assert len(log1["hash"]) == 64

@pytest.mark.asyncio
async def test_governance_capabilities():
    manager = GovernanceManager()
    
    # 1. PM can override risk
    assert manager.check_permission("PM", "override_risk") is True
    # 2. Trader cannot override risk
    assert manager.check_permission("TRADER", "override_risk") is False

@pytest.mark.asyncio
async def test_compliance_restrictions():
    manager = ComplianceControlsManager()
    
    # 1. restricted check
    assert manager.verify_symbol("XYZ") is False
    # 2. normal check
    assert manager.verify_symbol("TSLA") is True

@pytest.mark.asyncio
async def test_market_surveillance_patterns():
    engine = MarketSurveillance()
    
    # 1. Wash trading check
    trades = [
        {"buyer_id": "U1", "seller_id": "U2"},
        {"buyer_id": "U1", "seller_id": "U1"} # buyer == seller
    ]
    assert engine.check_wash_trading(trades) is True

    # 2. Spoofing check
    orders = [
        {"action": "CANCEL", "duration_ms": 100} # cancel under 500ms
    ]
    assert engine.check_spoofing(orders) is True

@pytest.mark.asyncio
async def test_policy_engine_routing():
    engine = CompliancePolicyEngine()
    
    # 1. Warning limit
    res_warn = engine.evaluate_order("AAPL", quantity=6000)
    assert res_warn["policy_action"] == "WARN"

    # 2. Escalate limit
    res_esc = engine.evaluate_order("AAPL", quantity=15000)
    assert res_esc["policy_action"] == "ESCALATE"

@pytest.mark.asyncio
async def test_explainability_justifications():
    explainer = ComplianceExplainer()
    res = explainer.explain_decision("DEC_123")
    
    assert res["decision_id"] == "DEC_123"
    assert "justified" in res["explanation"]

@pytest.mark.asyncio
async def test_retention_rules():
    manager = ComplianceRetentionManager()
    assert manager.get_retention_period("audit_records") == 7
    assert manager.get_retention_period("ops_logs") == 1
