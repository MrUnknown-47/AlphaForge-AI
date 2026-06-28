from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config import settings
from app.shared.database import db_manager
from app.shared.cache import cache_manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Map sync psycopg2 to async asyncpg engine for DB manager async pool
    db_url = settings.DATABASE_URL.replace("psycopg2", "asyncpg")
    db_manager.init(db_url)
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

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "alphaforge-backend"}