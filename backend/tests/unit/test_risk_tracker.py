import pytest
from app.modules.validation.risk_tracker import RiskTracker

def test_risk_tracker_var_cvar():
    tracker = RiskTracker()
    # Populate history returns to test VaR / CVaR calculations
    for ret in [-0.01, -0.02, 0.005, 0.012, -0.008, 0.015, -0.025]:
        tracker.add_return(ret)
        
    var_val, cvar_val = tracker.calculate_var_cvar(confidence_level=0.95)
    assert var_val < 0.0
    assert cvar_val <= var_val
