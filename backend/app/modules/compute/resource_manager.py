from typing import Dict, Any

class ComputeResourceManager:
    def __init__(self) -> None:
        pass

    def allocate_resources(self, job_id: str, cores_requested: int) -> bool:
        """Approves resource request if core count falls within limits (e.g. <= 32)."""
        return cores_requested <= 32
