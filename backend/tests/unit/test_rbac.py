import pytest
from app.modules.security.rbac_manager import RBACManager

def test_rbac_permissions():
    rbac = RBACManager()
    
    # ADMIN full access
    assert rbac.has_permission("ADMIN", "execute_trades") is True
    assert rbac.has_permission("ADMIN", "manage_secrets") is True

    # TRADER execution but no secrets
    assert rbac.has_permission("TRADER", "execute_trades") is True
    assert rbac.has_permission("TRADER", "manage_secrets") is False

    # VIEWER read-only
    assert rbac.has_permission("VIEWER", "view_dashboard") is True
    assert rbac.has_permission("VIEWER", "execute_trades") is False

    # AUDITOR reports access
    assert rbac.has_permission("AUDITOR", "read_reports") is True
    assert rbac.has_permission("AUDITOR", "execute_trades") is False
