from typing import Dict, Any, List

class ModelVersioning:
    def __init__(self) -> None:
        pass

    def get_version_lineage(self, name: str) -> List[str]:
        return [f"{name}-v1.0.0", f"{name}-v1.1.0", f"{name}-v2.0.0", f"{name}-v2.1.0"]
