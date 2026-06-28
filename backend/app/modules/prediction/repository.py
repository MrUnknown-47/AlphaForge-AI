import logging
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.prediction.models import (
    ModelRegistryModel,
    PredictionsModel,
    PredictionMetricsModel,
    ExplanationsModel
)

logger = logging.getLogger(__name__)

class PredictionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def register_new_model(
        self, model_name: str, version: str, hyperparameters: dict | None, storage_path: str | None
    ) -> ModelRegistryModel:
        # Deactivate previous versions of same model name
        stmt_deactivate = (
            update(ModelRegistryModel)
            .where(ModelRegistryModel.model_name == model_name)
            .values(is_active=False)
        )
        await self.db.execute(stmt_deactivate)

        model = ModelRegistryModel(
            model_name=model_name,
            version=version,
            hyperparameters=hyperparameters,
            storage_path=storage_path,
            is_active=True
        )
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return model

    async def get_active_model_by_name(self, model_name: str) -> ModelRegistryModel | None:
        stmt = select(ModelRegistryModel).where(
            ModelRegistryModel.model_name == model_name,
            ModelRegistryModel.is_active == True
        )
        res = await self.db.execute(stmt)
        return res.scalars().first()

    async def insert_predictions_batch(self, preds: list[dict]) -> None:
        if not preds:
            return
        
        # Prepare list of dictionaries matching model attributes
        values = [
            {
                "time": p["time"],
                "ticker": p["ticker"],
                "horizon": p["horizon"],
                "predicted_value": float(p["predicted_value"]),
                "confidence_lower": float(p["confidence_lower"]),
                "confidence_upper": float(p["confidence_upper"])
            }
            for p in preds
        ]
        
        stmt = insert(PredictionsModel)
        try:
            await self.db.execute(stmt, values)
            await self.db.commit()
            logger.info(f"Successfully batch-inserted {len(preds)} predictions to DB.")
        except Exception as e:
            await self.db.rollback()
            logger.warning(f"Batch insert for predictions failed: {e}. Attempting slow merge...")
            for val in values:
                stmt_select = select(PredictionsModel).where(
                    PredictionsModel.time == val["time"],
                    PredictionsModel.ticker == val["ticker"],
                    PredictionsModel.horizon == val["horizon"]
                )
                res = await self.db.execute(stmt_select)
                existing = res.scalars().first()
                if not existing:
                    new_pred = PredictionsModel(**val)
                    self.db.add(new_pred)
            await self.db.commit()

    async def insert_metrics_batch(self, metrics: list[dict]) -> None:
        if not metrics:
            return
        stmt = insert(PredictionMetricsModel)
        await self.db.execute(stmt, metrics)
        await self.db.commit()

    async def get_latest_predictions(self, ticker: str, horizon: str, limit: int = 20) -> list[PredictionsModel]:
        stmt = (
            select(PredictionsModel)
            .where(PredictionsModel.ticker == ticker, PredictionsModel.horizon == horizon)
            .order_by(PredictionsModel.time.desc())
            .limit(limit)
        )
        res = await self.db.execute(stmt)
        return list(res.scalars().all())

    async def insert_explanation_record(
        self, model_id: str, ticker: str, importances: dict, pdp: dict, drift: dict
    ) -> ExplanationsModel:
        explanation = ExplanationsModel(
            model_id=model_id,
            ticker=ticker,
            feature_importances=importances,
            partial_dependence=pdp,
            drift_metrics=drift
        )
        self.db.add(explanation)
        await self.db.commit()
        await self.db.refresh(explanation)
        return explanation

    async def get_latest_explanation(self, ticker: str) -> ExplanationsModel | None:
        stmt = (
            select(ExplanationsModel)
            .where(ExplanationsModel.ticker == ticker)
            .order_by(ExplanationsModel.created_at.desc())
        )
        res = await self.db.execute(stmt)
        return res.scalars().first()