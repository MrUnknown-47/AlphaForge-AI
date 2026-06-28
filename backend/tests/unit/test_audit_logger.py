import os
import json
import pytest
from app.modules.operations.audit_logger import AuditLogger

def test_audit_logger_files():
    logger = AuditLogger()
    path = logger.log_action("live_trading", {"ticker": "AAPL", "action": "BUY"})
    
    assert os.path.exists(path)
    with open(path, "r") as f:
        data = json.load(f)
        assert data["component"] == "live_trading"
        assert data["payload"]["ticker"] == "AAPL"

    # Clean up test audit file
    if os.path.exists(path):
        os.remove(path)
