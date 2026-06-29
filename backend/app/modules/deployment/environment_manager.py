from typing import Dict, Any, List

class EnvironmentManager:
    def __init__(self) -> None:
        self.environments = {
            "development": {"db_url": "localhost:5432/dev", "debug": True},
            "staging": {"db_url": "staging-db:5432/staging", "debug": False},
            "paper": {"db_url": "paper-db:5432/paper", "debug": False},
            "production": {"db_url": "prod-db-cluster:5432/prod", "debug": False}
        }

    def get_env_config(self, env: str) -> Dict[str, Any]:
        return self.environments.get(env.lower(), {"db_url": "localhost:5432/dev", "debug": True})
