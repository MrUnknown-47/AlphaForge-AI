import logging
from typing import Dict, Any

logger = logging.getLogger("FeatureIngestion")

class FeatureIngestionService:
    def __init__(self) -> None:
        pass

    def ingest_feature_value(self, feature_name: str, entity_id: str, value: float) -> None:
        logger.info(f"Ingested feature: {feature_name} for entity: {entity_id} value: {value}")
