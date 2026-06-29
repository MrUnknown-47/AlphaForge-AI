from typing import Dict, Any

class SecurityVault:
    def __init__(self) -> None:
        self.secrets = {
            "ALPACA_API_KEY": "encrypted_alpaca_key_hash",
            "POLYGON_API_KEY": "encrypted_polygon_key_hash",
            "POSTGRES_PASSWORD": "encrypted_postgres_password_hash"
        }

    def read_secret(self, key: str) -> str:
        return self.secrets.get(key, "NOT_FOUND")

    def write_secret(self, key: str, val: str) -> None:
        self.secrets[key] = val
