# Model Card: AlphaForge Ensemble

## Model Details
* **Ensemble type:** 70% XGBoost Classifier + 30% LSTM Network.
* **Objective:** Short-term trend class prediction (BUY/SELL/HOLD).

---

## Intended Use
* Designed for low-latency statistical arbitrage.
* Intended for paper trading or shadow validation. Not for unhedged live executions.

---

## Limitations & Risks
* **Regime shift vulnerabilities:** Performance decay expected under high-volatility shifts or black-swan macro events.
* **Drift risks:** Retraining cycles must be ran every 30 days to limit parameter drift.
