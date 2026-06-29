from typing import Dict, Any
from app.modules.security.vault import SecurityVault

class SecretManager:
    def __init__(self) -> None:
        self.vault = SecurityVault()

    def get_secret(self, name: str) -> str:
        return self.vault.read_secret(name)
