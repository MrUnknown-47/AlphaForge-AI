import pytest
from app.modules.shadow_validation.capacity_monitor import CapacityMonitor

def test_capacity_scaling_simulation():
    monitor = CapacityMonitor()
    tiers = monitor.simulate_capacity()
    
    assert len(tiers) == 5
    assert tiers[0]["capital_tier"] == 1000.0
    assert tiers[0]["capacity_decay_pct"] == 0.0
    assert tiers[4]["capital_tier"] == 500000.0
    assert tiers[4]["capacity_decay_pct"] == 15.0
