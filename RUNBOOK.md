# Operational incident Runbooks

This guide outlines action paths for live system incident management.

---

## 1. Broker Outage Remediation
If execution broker signals a timeout (> 2000ms) or disconnect:
1. Verify API status dashboard of vendor.
2. Route trade signals to shadow validation paper trading log mode.
3. Switch execution keys to secondary backup broker.

---

## 2. Model Drift Recovery
If PSI metrics exceed 0.10 limits:
1. Trigger automatic walk-forward optimization runs across current datasets.
2. Retrain XGBoost parameter models.
3. Lock live trading weights to baseline v1.0.0.
