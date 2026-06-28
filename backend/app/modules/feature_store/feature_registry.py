from typing import Callable, Any
from app.modules.feature_store.exceptions import FeatureNotFoundException
from app.modules.feature_store.schemas import FeatureMetadata

class FeatureDefinition:
    def __init__(self, metadata: FeatureMetadata, compute_fn: Callable[..., Any]):
        self.metadata = metadata
        self.compute_fn = compute_fn

class FeatureRegistry:
    def __init__(self) -> None:
        self._registry: dict[str, FeatureDefinition] = {}

    def register_feature(self, metadata: FeatureMetadata, compute_fn: Callable[..., Any]) -> None:
        self._registry[metadata.name.upper()] = FeatureDefinition(metadata, compute_fn)

    def get_feature(self, name: str) -> FeatureDefinition:
        definition = self._registry.get(name.upper())
        if not definition:
            raise FeatureNotFoundException(f"Feature '{name}' is not registered")
        return definition

    def list_features(self) -> list[str]:
        return list(self._registry.keys())

feature_registry = FeatureRegistry()
