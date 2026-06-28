import os
from typing import Dict, Any, List

class SecretsManager:
    def __init__(self) -> None:
        self.sensitive_keys = {
            "POLYGON_API_KEY", "ALPACA_KEY", "ALPACA_SECRET", "JWT_SECRET", "DATABASE_PASSWORD"
        }

    def validate_env(self) -> List[str]:
        missing = []
        for key in self.sensitive_keys:
            if key not in os.environ and not getattr(self, "_mock_override", False):
                missing.append(key)
        return missing

    def mask_secret(self, secret: str) -> str:
        if not secret or len(secret) < 6:
            return "******"
        return f"{secret[:3]}...{secret[-3:]}"

    def get_masked_secrets(self) -> Dict[str, str]:
        masked = {}
        for key in self.sensitive_keys:
            val = os.environ.get(key, "dummy_value_for_testing")
            masked[key] = self.mask_secret(val)
        return masked
