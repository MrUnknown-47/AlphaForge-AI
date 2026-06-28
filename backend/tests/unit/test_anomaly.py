import pytest
from app.modules.security.anomaly_detector import AnomalyDetector

def test_anomaly_inspections():
    detector = AnomalyDetector()
    
    # Healthy checks (no anomalies)
    assert len(detector.inspect_traffic(1.2, 0.25, 45.0, 1)) == 0

    # Critical trade frequency spike
    anoms = detector.inspect_traffic(12.5, 0.25, 45.0, 1)
    assert len(anoms) == 1
    assert anoms[0]["type"] == "ORDER_FREQUENCY_SPIKE"

    # Consecutive login failures abuse
    anoms_login = detector.inspect_traffic(1.2, 0.25, 45.0, 7)
    assert len(anoms_login) == 1
    assert anoms_login[0]["type"] == "LOGIN_ABUSE_ATTEMPT"
