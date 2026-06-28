from app.shared.exceptions import AlphaForgeException

class PredictionException(AlphaForgeException):
    """Base custom exception for the Prediction domain."""
    status_code: int = 400
    detail: str = "Prediction pipeline operations error"

class ModelTrainingFailedException(PredictionException):
    status_code: int = 500
    detail: str = "Model training execution failed"

class ModelNotFoundException(PredictionException):
    status_code: int = 404
    detail: str = "Requested prediction model was not registered"