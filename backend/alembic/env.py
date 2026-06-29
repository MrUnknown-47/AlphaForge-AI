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
from app.modules.market_data.models import SymbolModel, Ohlcv1mModel, PolygonQuoteModel, PolygonTradeModel, PolygonBarModel, PolygonOptionsChainModel
from app.modules.portfolio.models import PortfolioModel, PortfolioAccountModel, PortfolioPositionModel, PortfolioOrderModel, PortfolioSnapshotModel, PortfolioMetricsHistoryModel, PortfolioAllocationModel, PortfolioRiskMetricsModel
from app.modules.live_trading.db_models import ExecutionOrderModel, ExecutionFillModel, ExecutionPositionModel, ExecutionTelemetryModel, ExecutionPnlModel, ExecutionSlippageModel, ExecutionEventModel, ExecutionSessionModel
from app.modules.backtesting.db_models import BacktestStrategyModel, BacktestRunModel, BacktestOrderModel, BacktestTradeModel, BacktestPositionModel, BacktestSnapshotModel, BacktestMetricsModel, BacktestOptimizationModel, BacktestWalkforwardModel, BacktestMontecarloModel
from app.modules.research.db_models import ResearchFactorModel, ResearchFeatureModel, ResearchFactorExposureModel, ResearchValidationModel, ResearchRegimeModel, ResearchCorrelationModel, ResearchClusterModel, ResearchExplanationModel, ResearchOptimizationModel, ResearchReportModel
from app.modules.ai.db_models import AiAgentModel, AiDebateModel, AiDecisionModel, AiMemoryModel, AiEmbeddingModel, AiExplanationModel, AiReportModel, AiCommitteeModel, AiRecommendationModel
from app.modules.ml.db_models import MlModel, MlTrainingRunModel, MlPredictionModel, MlDriftModel, MlFeatureModel, MlForecastModel, MlExplanationModel, MlRegistryModel, MlMetricsModel
from app.modules.risk.db_models import RiskVarModel, RiskCvarModel, RiskStressModel, RiskScenarioModel, RiskExposureModel, RiskDrawdownModel, RiskCorrelationModel, RiskContagionModel, RiskLiquidityModel, RiskLimitModel, RiskEventModel, RiskReportModel
from app.modules.operations.db_models import OpsMetricsModel, OpsLogsModel, OpsAlertsModel, OpsIncidentsModel, OpsTelemetryModel, OpsTracesModel, OpsHealthModel, OpsEventsModel, OpsServicesModel, OpsReportsModel, NOCModel
from app.modules.compliance.db_models import ComplianceAuditLog, ComplianceEvent, ComplianceApproval, CompliancePolicy, ComplianceControl, ComplianceAttestation, CompliancePermission, ComplianceExplanation, ComplianceReport, ComplianceRetention
from app.modules.shadow.db_models import ShadowRunModel, ShadowReconciliationModel, ShadowExecutionQualityModel, ShadowAttributionModel

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
