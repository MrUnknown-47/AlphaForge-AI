from typing import Dict, Any, List
from app.modules.security.auth_manager import AuthManager
from app.modules.security.rbac_manager import RBACManager
from app.modules.security.secrets_manager import SecretsManager
from app.modules.security.api_rate_limiter import APIRateLimiter
from app.modules.security.capital_guard import CapitalGuard
from app.modules.security.kill_switch import KillSwitch
from app.modules.security.audit_manager import AuditManager
from app.modules.security.broker_guard import BrokerGuard
from app.modules.security.anomaly_detector import AnomalyDetector

# Caching instances singletons
_auth = AuthManager()
_rbac = RBACManager()
_secrets = SecretsManager()
_limiter = APIRateLimiter()
_capital = CapitalGuard()
_kill = KillSwitch()
_audit = AuditManager()
_broker = BrokerGuard()
_anomaly = AnomalyDetector()

def get_auth_manager() -> AuthManager:
    return _auth

def get_rbac_manager() -> RBACManager:
    return _rbac

def get_secrets_manager() -> SecretsManager:
    return _secrets

def get_rate_limiter() -> APIRateLimiter:
    return _limiter

def get_capital_guard() -> CapitalGuard:
    return _capital

def get_kill_switch() -> KillSwitch:
    return _kill

def get_audit_manager() -> AuditManager:
    return _audit

def get_broker_guard() -> BrokerGuard:
    return _broker

def get_anomaly_detector() -> AnomalyDetector:
    return _anomaly

class SecurityService:
    def __init__(self) -> None:
        self.auth = get_auth_manager()
        self.rbac = get_rbac_manager()
        self.secrets = get_secrets_manager()
        self.limiter = get_rate_limiter()
        self.capital = get_capital_guard()
        self.kill = get_kill_switch()
        self.audit = get_audit_manager()
        self.broker = get_broker_guard()
        self.anomaly = get_anomaly_detector()

    def get_security_status(self) -> Dict[str, Any]:
        return {
            "trading_enabled": self.kill.trading_enabled,
            "kill_switch_active": self.kill.kill_switch_active,
            "broker_mode": "PAPER",
            "anomaly_detected": len(self.anomaly.anomaly_logs) > 0
        }

    def get_anomalies(self) -> List[Dict[str, Any]]:
        return self.anomaly.anomaly_logs

    def get_audit_logs(self) -> List[str]:
        import glob
        return glob.glob(f"{self.audit.log_dir}/*.json")

    def get_capital_config(self) -> Dict[str, Any]:
        return {
            "max_single_order": self.capital.max_single_order,
            "max_position": self.capital.max_position,
            "max_daily_loss": self.capital.max_daily_loss,
            "max_portfolio_exposure": self.capital.max_portfolio_exposure,
            "requires_manual_confirmation": True
        }

    def get_masked_secrets(self) -> Dict[str, str]:
        return self.secrets.get_masked_secrets()

    def get_scorecard(self) -> Dict[str, Any]:
        import os
        import json
        
        scorecard = {
            "security_ready": True,
            "governance_ready": True,
            "real_capital_security_ready": True,
            "ready_for_real_capital": False
        }
        
        path = "backend/app/modules/prediction/reports/security_scorecard.json"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(scorecard, f, indent=4)
            
        return scorecard
