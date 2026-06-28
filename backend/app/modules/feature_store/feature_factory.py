from app.modules.feature_store.feature_registry import feature_registry, FeatureDefinition

class FeatureFactory:
    @staticmethod
    def get_feature_runner(name: str) -> FeatureDefinition:
        """
        Resolves feature registration mapping.
        """
        return feature_registry.get_feature(name)
