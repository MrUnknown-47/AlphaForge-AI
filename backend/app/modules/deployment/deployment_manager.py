import logging
from typing import Dict, Any, List

logger = logging.getLogger("DeploymentManager")

class DeploymentManager:
    def __init__(self) -> None:
        self.active_version = "v1.2.0-prod"
        self.history = [
            {"version": "v1.2.0-prod", "status": "ACTIVE", "environment": "production"},
            {"version": "v1.2.0-rc2", "status": "STANDBY", "environment": "staging"},
            {"version": "v1.1.9-prod", "status": "ROLLED_BACK", "environment": "production"}
        ]

    def get_deployments(self) -> List[Dict[str, Any]]:
        return self.history

    def deploy_new_version(self, version: str, env: str) -> Dict[str, Any]:
        new_release = {"version": version, "status": "ACTIVE", "environment": env}
        # Update current active in history
        for item in self.history:
            if item["environment"] == env and item["status"] == "ACTIVE":
                item["status"] = "INACTIVE"
                
        self.history.insert(0, new_release)
        if env == "production":
            self.active_version = version
        logger.info(f"Deployed new version: {version} to environment: {env}")
        return new_release
