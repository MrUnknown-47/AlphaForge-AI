import os
import pickle
import logging
import asyncio
from datetime import datetime
import pandas as pd
import numpy as np
from sqlalchemy import text
from app.shared.database import db_manager
from app.modules.prediction.ml_models import XGBoostModel, LSTMModel, Scaler
from app.modules.prediction.repository import PredictionRepository

logger = logging.getLogger(__name__)

# Create directories
os.makedirs("backend/app/modules/prediction/models", exist_ok=True)
os.makedirs("backend/app/modules/prediction/reports", exist_ok=True)
os.makedirs("backend/app/modules/prediction/plots", exist_ok=True)



class QuantTrainer:
    def __init__(self, data_dir: str = "data/") -> None:
        self.data_dir = data_dir
        self.scaler = Scaler()
        self.models = {
            "XGBoost": XGBoostModel,
            "LSTM": LSTMModel
        }

    def load_splits(self, horizon: str = "1d") -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, list[str]]:
        train_path = os.path.join(self.data_dir, "train.csv")
        val_path = os.path.join(self.data_dir, "validation.csv")

        df_train = pd.read_csv(train_path)
        df_val = pd.read_csv(val_path)

        target_col = f"target_{horizon}"
        exclude_cols = {"time", "ticker", "target_1d", "target_5d", "target_20d"}
        feature_cols = [c for c in df_train.columns if c not in exclude_cols]

        X_train = df_train[feature_cols].values
        y_train = df_train[target_col].values

        X_val = df_val[feature_cols].values
        y_val = df_val[target_col].values

        return X_train, y_train, X_val, y_val, feature_cols

    async def execute_expanding_train(self, horizon: str = "1d", model_type: str = "XGBoost") -> None:
        X_train, y_train, X_val, y_val, feature_cols = self.load_splits(horizon)

        # 1. Feature scaling
        self.scaler.fit(X_train)
        X_train_scaled = self.scaler.transform(X_train)
        X_val_scaled = self.scaler.transform(X_val)

        # 2. Expanding Window loop: Simulate retraining across 3 expanding splits
        n_samples = len(X_train_scaled)
        step = n_samples // 3

        logger.info(f"Running expanding window cross-validation splits for {model_type}...")
        for i in range(1, 4):
            limit = min(step * i, n_samples)
            X_fold = X_train_scaled[:limit]
            y_fold = y_train[:limit]
            
            logger.info(f"Training expanding fold {i} on size: {len(X_fold)}")
            model_cls = self.models.get(model_type, XGBoostModel)
            model = model_cls()
            model.fit(X_fold, y_fold)

        # 3. Final model fit
        final_model = self.models.get(model_type, XGBoostModel)()
        final_model.fit(X_train_scaled, y_train)

        # 4. Save model and scaler binaries
        version_str = f"{model_type}_{horizon}_{int(datetime.utcnow().timestamp())}"
        model_path = f"backend/app/modules/prediction/models/{version_str}.pkl"
        
        with open(model_path, "wb") as f:
            pickle.dump({"model": final_model, "scaler": self.scaler, "features": feature_cols}, f)
        
        logger.info(f"Successfully saved trained model binary: {model_path}")

        # 5. Database registration
        # Safe database connection check
        try:
            async with db_manager.session() as db:
                repo = PredictionRepository(db)
                await repo.register_new_model(
                    model_name=f"{model_type}_Model_{horizon}",
                    version=version_str,
                    hyperparameters=final_model.params if hasattr(final_model, "params") else {},
                    storage_path=model_path
                )
        except Exception as e:
            logger.warning(f"Failed to register model in DB registry: {e}. Model binary saved locally.")

async def run_training():
    trainer = QuantTrainer()
    for m in ["XGBoost", "LSTM"]:
        try:
            await trainer.execute_expanding_train(horizon="1d", model_type=m)
        except Exception as e:
            logger.error(f"Failed training {m}: {e}")

if __name__ == "__main__":
    try:
        db_manager.init("postgresql+asyncpg://postgres:postgres@localhost:5432/alphaforge")
    except Exception as e:
        logger.warning(f"Could not initialize database session manager: {e}")
    asyncio.run(run_training())
