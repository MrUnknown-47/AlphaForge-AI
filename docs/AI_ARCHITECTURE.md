# AlphaForge AI Modeling & AI Architecture

This document describes the design of the forecasting ensembles, feature stores, and agent pipelines.

---

## 1. Ensemble Prediction Model (0.7 XGBoost + 0.3 LSTM)

To balance robust trend indicators with temporal sequence dependencies, predictions combine:
1. **XGBoost Classifier (70% weight):** Trained on static technical markers (EMA crossovers, RSI levels, VWAP deviations).
2. **LSTM Model (30% weight):** Retrained on sequence window arrays containing raw price variations to identify temporal autocorrelation.

---

## 2. SHAP Explainability Pipeline

Before a trade order ticket is issued, the signal is fed into a SHAP explainer to calculate marginal feature contributions:
* If the base likelihood is below threshold bounds, the execution engine cancels signal routing.
* Feature importance margins are displayed directly on the execution station desks.

---

## 3. RAG Document Vector Search

* **Embedding Model:** `SentenceTransformers` (all-MiniLM-L6-v2) producing 384-dimensional dense vectors.
* **Vector Index:** `FAISS` running L2 distance metrics to resolve nearest neighbors for user context questions.
