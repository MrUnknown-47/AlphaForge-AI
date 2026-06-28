# AlphaForge AI System Operations Guide

This document details the system monitoring, alert escalation paths, and model lifecycle operations.

---

## 1. MLOps Retraining & Drift Monitor

* **Feature Drift Indicator:** The system tracks the Population Stability Index (PSI) daily.
* **Retraining Triggers:** If PSI exceeds `0.10` bounds, the system marks the XGBoost models for retuning.
* **Auto-Retrain Cycle:** Every 30 days, models undergo walk-forward optimization runs across updated historical datasets.

---

## 2. Infrastructure Health Monitoring

* **Liveness Checks:** System endpoints `/health` verify Redis connection, database pool latency, and websocket heartbeat status.
* **Audit Logs:** Configuration edits, database schema mutations, and API key retrievals are stored chronologically inside read-only system logs.
