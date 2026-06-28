# AlphaForge AI System Architecture

This document maps out the system architecture and data pipelines for AlphaForge AI.

---

## 1. High-Level Data & Signal Flow

The diagram below outlines how market feeds flow into the feature stores, prediction engines, risk gates, and down to the broker execution layer.

```mermaid
graph TD
  Feed[Polygon / Alpaca Market Feed] --> FeatureStore[Feature Store / Cache]
  FeatureStore --> ML[Ensemble Model: XGBoost + LSTM]
  ML --> PredEngine[Prediction Engine]
  PredEngine --> RiskGate[Risk Manager / Capital Guard]
  RiskGate --> Broker[Broker Abstraction Layer]
  Broker --> Execution[Alpaca/Polygon API]
```

---

## 2. Multi-Agent Collaboration Workflow

Specialized research agents negotiate allocation targets inside the debate chamber before final supervisor deployment approval.

```mermaid
graph TD
  CIO[CIO Agent] --> Debate[Debate Chamber]
  Quant[Quant Agent] --> Debate
  Risk[Risk Agent] --> Debate
  Debate --> Consensus[Consensus Engine]
  Consensus --> Supervisor[Supervisor Approval Gate]
```

---

## 3. RAG Research Architecture

Embeddings index generation flow across unstructured corporate text reports.

```mermaid
graph TD
  Docs[SEC 10-Q / Earnings Transcripts] --> Chunking[Chunking Engine]
  Chunking --> Embedding[SentenceTransformers Embedding]
  Embedding --> FAISS[FAISS Vector Store]
  FAISS --> QueryEngine[RAG Query Retriever]
```
