import pytest
import numpy as np
from app.modules.validation.drift_tracker import DriftTracker

def test_drift_tracker_psi():
    tracker = DriftTracker()
    baseline = np.random.normal(0.0012, 0.012, 100)
    current = np.random.normal(0.0012, 0.012, 100)
    
    psi = tracker.calculate_psi(baseline, current)
    assert psi >= 0.0
