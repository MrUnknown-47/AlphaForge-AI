import asyncio
import sys
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context

# Add current path to sys.path so alembic can resolve app package
import os
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from app.config import settings
from app.shared.database import Base

# Import all models to register metadata
from app.modules.auth.models import UserModel, SessionModel, RevokedTokenModel
from app.modules.derivatives.models import OptionContractModel, FuturesContractModel
from app.modules.feature_store.models import TechnicalFeaturesModel, MarketFeaturesModel, FundamentalFeaturesModel, SentimentFeaturesModel
from app.modules.fundamental.models import FinancialStatementModel

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    import re
    url = settings.DATABASE_URL.replace("psycopg2", "asyncpg")
    if "sslmode=" in url:
        url = url.replace("sslmode=require", "ssl=require")
    url = re.sub(r'[&?]channel_binding=[^&]+', '', url)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online() -> None:
    import re
    url = settings.DATABASE_URL.replace("psycopg2", "asyncpg")
    if "sslmode=" in url:
        url = url.replace("sslmode=require", "ssl=require")
    url = re.sub(r'[&?]channel_binding=[^&]+', '', url)
    connectable = create_async_engine(url)
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
