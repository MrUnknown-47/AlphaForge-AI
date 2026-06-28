# AlphaForge AI

AlphaForge AI is an institutional-grade quantitative trading, AI copilot, and multi-agent portfolio optimization workstation.

## Overview

AlphaForge AI integrates machine learning ensembles (0.7 XGBoost + 0.3 LSTM) with real-time market data providers, secure broker abstraction layers, RAG research terminals, and capital protection safeguards.

### Core Systems

1. **Quant Trading Platform:** Real-time data streaming and automated signal execution.
2. **AI Copilot & Multi-Agent Desk:** Collaboration of specialized agents (CIO, PM, Quant, Risk).
3. **RAG Research Terminal:** Semantic search across SEC filings and earnings call transcripts.
4. **Portfolio Analytics & Optimization:** Aladdin-style risk metrics and HRP rebalancing.
5. **Hedge Fund Simulator:** Multi-book AUM leverage simulator and stress test environment.

---

## Architecture

For a detailed walkthrough of the backend and frontend topology systems, please refer to the [System Architecture Guide](file:///Users/vaibhavsingh/stock/docs/ARCHITECTURE.md).

---

## Installation & Setup

### Environment Variables
Copy `.env.example` to `.env` and fill in API secrets:
```bash
cp .env.example .env
```

### Local Development

1. **Backend Service:**
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

2. **Frontend Workstation:**
```bash
cd frontend
npm install
npm run dev
```

3. **Running Tests:**
```bash
pytest backend/tests/
```

## License

This project is licensed under the Apache-2.0 License.
See the LICENSE file for details.
