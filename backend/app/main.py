from fastapi import FastAPI
from app.config import settings
from app.modules.broker.router import router as broker_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0-MVP",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Register endpoints routers
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

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "alphaforge-backend"}