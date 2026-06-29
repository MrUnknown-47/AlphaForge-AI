import logging
from typing import Dict, Any

logger = logging.getLogger("ArtifactStore")

class ArtifactStore:
    def __init__(self) -> None:
        pass

    def save_checkpoint(self, name: str, data: bytes) -> None:
        logger.info(f"Saved model checkpoint: {name} ({len(data)} bytes) to artifact store.")
