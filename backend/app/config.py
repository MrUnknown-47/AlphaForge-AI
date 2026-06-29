from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AlphaForge AI Monolith"
    DATABASE_URL: str = "postgresql+asyncpg://neondb_owner:npg_B9tvpliXs8hZ@ep-patient-dew-aobozvzr-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    REDIS_URL: str = "redis://localhost:6379/0"
    SECRET_KEY: str = "supersecretkeychangeinproduction"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ENVIRONMENT: str = "local"
    
    # Extra inputs loaded from local .env
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    finbert_model_name: str = "yiyanghkust/finbert-tone"
    faiss_index_path: str = "/workspace/research/faiss_index"

    # API Keys for Data Providers
    POLYGON_API_KEY: str = ""
    POLYGON_BASE_URL: str = "https://api.polygon.io"
    POLYGON_WS_URL: str = "wss://socket.polygon.io"
    ALPACA_API_KEY: str = ""
    ALPACA_API_SECRET: str = ""
    TWELVEDATA_API_KEY: str = ""
    
    # Broker Abstraction Layer Configuration
    BROKER: str = "PAPER"
    ALPACA_KEY: str = ""
    ALPACA_SECRET: str = ""
    PAPER_STARTING_CAPITAL: float = 100000.0
    
    class Config:
        env_file = ".env"
        extra = "ignore" # Ignore extra keys in .env to prevent validation failures

settings = Settings()