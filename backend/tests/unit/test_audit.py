import os
import json
import pytest
from app.modules.security.audit_manager import AuditManager

def test_audit_logs():
    manager = AuditManager()
    path = manager.log_entry(
        username="admin_user", role="ADMIN", ip="127.0.0.1", endpoint="/orders",
        action="EXECUTE_TRADE", details={"ticker": "AAPL", "qty": 10}
    )
    
    assert os.path.exists(path)
    with open(path, "r") as f:
        data = json.load(f)
        assert data["user"] == "admin_user"
        assert data["role"] == "ADMIN"
        assert data["ip"] == "127.0.0.1"

    # Clean up test audit log file
    if os.path.exists(path):
        os.remove(path)
