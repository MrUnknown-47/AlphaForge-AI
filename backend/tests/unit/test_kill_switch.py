import pytest
from app.modules.security.kill_switch import KillSwitch

def test_kill_switch_triggers():
    ks = KillSwitch()
    
    # Healthy conditions
    healthy = {
        "drawdown": -0.05,
        "daily_loss_pct": 0.01,
        "broker_online": True,
        "db_online": True,
        "psi": 0.05,
        "sharpe": 1.5,
        "hit_ratio": 0.60,
        "reconciliation_ok": True
    }
    assert ks.evaluate_state(healthy) is True
    assert ks.trading_enabled is True

    # Violate database offline condition
    unhealthy_db = healthy.copy()
    unhealthy_db["db_online"] = False
    assert ks.evaluate_state(unhealthy_db) is False
    assert ks.trading_enabled is False

    # Violate drawdown limit (>20%)
    ks_dd = KillSwitch()
    unhealthy_dd = healthy.copy()
    unhealthy_dd["drawdown"] = -0.22
    assert ks_dd.evaluate_state(unhealthy_dd) is False
    assert ks_dd.trading_enabled is False
