from app.shared.exceptions import AlphaForgeException

class FeatureStoreException(AlphaForgeException):
    status_code: int = 400
    detail: str = "Feature store platform error"

class FeatureNotFoundException(FeatureStoreException):
    status_code: int = 404
    detail: str = "Requested feature name is not defined in the registry"

class FeatureValidationFailed(FeatureStoreException):
    status_code: int = 422
    detail: str = "Calculated features failed sanity checks (outliers or high null ratio)"

class BackfillJobException(FeatureStoreException):
    status_code: int = 500
    detail: str = "Feature backfill operation encountered a processing exception"