from typing import Dict, Any, List
from app.modules.security.service import SecurityService

class SecurityFacade:
    def __init__(self) -> None:
        self.service = SecurityService()

    def get_status(self) -> Dict[str, Any]:
        return self.service.get_security_status()

    def get_audit(self) -> List[str]:
        return self.service.get_audit_logs()

    def get_anomalies(self) -> List[Dict[str, Any]]:
        return self.service.get_anomalies()

    def get_kill_switch_state(self) -> Dict[str, Any]:
        status = self.service.get_security_status()
        return {
            "trading_enabled": status["trading_enabled"],
            "kill_switch_active": status["kill_switch_active"]
        }

    def get_capital(self) -> Dict[str, Any]:
        return self.service.get_capital_config()

    def get_secrets(self) -> Dict[str, str]:
        return self.service.get_masked_secrets()

    def get_scorecard(self) -> Dict[str, Any]:
        return self.service.get_scorecard()
