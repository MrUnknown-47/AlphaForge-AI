from typing import Dict, Any, List

class RoleAccessControl:
    def __init__(self) -> None:
        self.role_privileges = {
            "ADMIN": ["read_secrets", "write_secrets", "rotate_secrets", "failover_clusters"],
            "COMPLIANCE": ["read_secrets"],
            "TRADER": ["read_secrets"]
        }

    def verify_privilege(self, role: str, privilege: str) -> bool:
        return privilege in self.role_privileges.get(role.upper(), [])
