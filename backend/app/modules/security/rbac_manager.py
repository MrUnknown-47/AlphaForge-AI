from typing import Dict, Set

class RBACManager:
    def __init__(self) -> None:
        self.role_permissions: Dict[str, Set[str]] = {
            "ADMIN": {
                "execute_trades", "view_positions", "view_dashboard", "read_logs", "read_reports", "manage_secrets"
            },
            "TRADER": {
                "execute_trades", "view_positions", "view_dashboard"
            },
            "VIEWER": {
                "view_dashboard"
            },
            "AUDITOR": {
                "read_logs", "read_reports"
            }
        }

    def has_permission(self, role: str, permission: str) -> bool:
        permissions = self.role_permissions.get(role.upper(), set())
        return permission in permissions
