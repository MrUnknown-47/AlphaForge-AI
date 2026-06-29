from typing import List

class GovernanceManager:
    def __init__(self) -> None:
        # Roles: ADMIN, CIO, PM, TRADER, RISK_MANAGER, RESEARCHER, AUDITOR
        self.role_permissions = {
            "ADMIN": ["all"],
            "CIO": ["all"],
            "PM": ["view", "trade", "override_risk"],
            "TRADER": ["view", "trade"],
            "RISK_MANAGER": ["view", "override_risk", "configure_limits"],
            "RESEARCHER": ["view", "backtest"],
            "AUDITOR": ["view_audit_logs"]
        }

    def check_permission(self, role: str, action: str) -> bool:
        perms = self.role_permissions.get(role, [])
        return "all" in perms or action in perms
