from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.shared.database import db_manager
from app.shared.cache import cache_manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_url = settings.DATABASE_URL.replace("psycopg2", "asyncpg")
    db_manager.init(db_url)
    
    # Enforce Neon PostgreSQL availability check on startup
    try:
        from sqlalchemy import text
        async with db_manager._engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
    except Exception as e:
        print(f"[STARTUP CRITICAL] Neon database connection failed: {e}")
        raise RuntimeError("Cannot connect to Neon PostgreSQL")
        
    cache_manager.init(settings.REDIS_URL)
    yield
    await db_manager.close()
    await cache_manager.close()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0-MVP",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Enforce CORS configuration BEFORE routing calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Register endpoints routers
from app.modules.auth.router import router as auth_router
app.include_router(auth_router)

from app.modules.broker.router import router as broker_router
app.include_router(broker_router)

from app.modules.live_trading.router import router as live_trading_router
app.include_router(live_trading_router)

from app.modules.copilot.router import router as copilot_router
app.include_router(copilot_router)

from app.modules.validation.router import router as validation_router
app.include_router(validation_router)

from app.modules.shadow_trading.router import router as shadow_trading_router
app.include_router(shadow_trading_router)

from app.modules.operations.router import router as operations_router
app.include_router(operations_router)

from app.modules.security.router import router as security_router
app.include_router(security_router)

from app.modules.shadow_validation.router import router as shadow_validation_router
app.include_router(shadow_validation_router)

from app.modules.derivatives.router import router as derivatives_router
app.include_router(derivatives_router)

from app.modules.execution.router import router as execution_router
app.include_router(execution_router)

from app.modules.market_data.polygon_router import router as polygon_market_router
app.include_router(polygon_market_router)

from app.modules.portfolio.sync_router import router as portfolio_sync_router
app.include_router(portfolio_sync_router)

from app.modules.live_trading.execution_router import router as live_execution_router
app.include_router(live_execution_router)

from app.modules.backtesting.backtest_router import router as backtest_router
app.include_router(backtest_router)

from app.modules.research.research_router import router as research_router
app.include_router(research_router)

from app.modules.ai.router import router as ai_router
app.include_router(ai_router)

from app.modules.ml.router import router as ml_router
app.include_router(ml_router)

from app.modules.risk.router import router as risk_stress_router
app.include_router(risk_stress_router)

from app.modules.compliance.router import router as compliance_router
app.include_router(compliance_router)

from app.modules.cio.router import router as cio_router
app.include_router(cio_router)

from app.modules.assets.router import router as assets_router
app.include_router(assets_router)

from app.modules.deployment.router import router as deployment_router
app.include_router(deployment_router)

from app.modules.compute.router import router as compute_router
app.include_router(compute_router)

from app.modules.feature_store.router import router as feature_store_router
app.include_router(feature_store_router)

from app.modules.experiments.router import router as experiments_router
app.include_router(experiments_router)

from app.modules.model_registry.router import router as model_registry_router
app.include_router(model_registry_router)

from app.modules.fund.router import router as fund_router
app.include_router(fund_router)

from app.modules.futures.router import router as futures_router
app.include_router(futures_router)

from app.modules.fx.router import router as fx_router
app.include_router(fx_router)

from app.modules.crypto.router import router as crypto_router
app.include_router(crypto_router)

from app.modules.shadow.router import router as shadow_router
app.include_router(shadow_router)

@app.get("/options")
async def get_root_options():
    return {
        "underlying": "AAPL",
        "options_chain": [
            {"strike": 145.0, "type": "PUT", "bid": 1.20, "ask": 1.25},
            {"strike": 150.0, "type": "CALL", "bid": 2.40, "ask": 2.45}
        ]
    }

@app.post("/options/strategy")
async def post_root_options_strategy(strategy_name: str, S: float, strike: float, premium: float):
    from app.modules.derivatives.strategies.service import OptionsStrategyService
    func = getattr(OptionsStrategyService, strategy_name.lower().replace(" ", "_"), None)
    if func:
        return func(S, strike, premium)
    return {"error": "Strategy not found"}

@app.get("/cross-risk")
async def get_root_cross_risk():
    return {
        "cross_asset_var_95": 0.054,
        "cross_gamma": 0.0012,
        "cross_vega": 0.0045,
        "portfolio_duration": 4.82,
        "convexity": 0.24,
        "correlation_matrix": {
            "EQUITY-BOND": -0.15,
            "EQUITY-CRYPTO": 0.62,
            "BOND-CRYPTO": -0.22
        },
        "contagion_matrix": {
            "EQUITY": 0.12,
            "BOND": 0.03,
            "CRYPTO": 0.28
        }
    }

@app.get("/macro-allocation")
async def get_root_macro_allocation():
    return {
        "timestamp": datetime.utcnow() if "datetime" in globals() else "2026-06-29T10:38:00Z",
        "allocations": {
            "Equities": 0.40,
            "Options": 0.10,
            "Futures": 0.15,
            "Forex": 0.10,
            "Crypto": 0.05,
            "Bonds": 0.15,
            "Commodities": 0.05
        },
        "volatility_target": 0.12,
        "risk_budgeting_active": True
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "alphaforge-backend"}