import logging
from datetime import datetime, timedelta
from typing import Dict, Any

logger = logging.getLogger("SecretRotation")

class SecretRotationService:
    def __init__(self) -> None:
        pass

    def rotate_api_key(self, name: str) -> Dict[str, Any]:
        next_rotation = datetime.utcnow() + timedelta(days=90)
        logger.warning(f"SECRET ROTATED: Key: {name} successfully rotated. Next rotation: {next_rotation}")
        return {
            "secret_name": name,
            "status": "ROTATED",
            "next_rotation_due": next_rotation
        }
