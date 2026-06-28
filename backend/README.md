# AlphaForge Backend Engine

This is the FastAPI quantitative execution backend server.

## Architecture & Pipelines

1. **Market Data Feed:** Subscribes to Polygon/Alpaca REST/Websocket streams and stores ticks inside regional databases.
2. **Feature Store:** Computes indicators (EMAs, VWAPs, RSI) and caches feature matrices in local cache vectors.
3. **Forecasting Ensemble:** Invokes the combined `0.7 XGBoost + 0.3 LSTM` model pipelines.
4. **Risk & Capital Guards:** Validates maximum position sizing, drawdown boundaries, and processes emergency circuit breakers.

---

## Directory Layout
* `app/main.py`: Base FastAPI router bootstrap.
* `app/modules/auth/`: JWT credential validations and MFA.
* `app/modules/security/`: Rate limiters, maskings, and kill switches.
* `app/modules/shadow_validation/`: 90-day shadow tracker engines.
* `app/modules/portfolio/`: HRP / Mean-variance portfolio rebalancers.

---

## Getting Started

1. **Active environment:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. **Start service:**
```bash
uvicorn app.main:app --reload --port 8000
```

## License

This project is licensed under the Apache-2.0 License.
See the LICENSE file for details.
