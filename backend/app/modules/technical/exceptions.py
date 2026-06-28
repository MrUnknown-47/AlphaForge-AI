from app.shared.exceptions import AlphaForgeException

class TechnicalException(AlphaForgeException):
    status_code: int = 400
    detail: str = "Technical indicators system error"

class IndicatorNotFoundException(TechnicalException):
    status_code: int = 404
    detail: str = "Requested indicator is not registered in the system"

class InsufficientDataException(TechnicalException):
    status_code: int = 400
    detail: str = "Insufficient historical price points available to compute values"

class InvalidParametersException(TechnicalException):
    status_code: int = 400
    detail: str = "Invalid parameters provided for indicator calculation (e.g. period <= 0)"