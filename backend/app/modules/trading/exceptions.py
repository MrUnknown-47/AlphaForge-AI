from app.shared.exceptions import AlphaForgeException

class TradingException(AlphaForgeException):
    status_code: int = 400
    detail: str = "Trading operations system error"

class OrderNotFoundException(TradingException):
    status_code: int = 404
    detail: str = "Specified order cannot be found"

class OrderValidationError(TradingException):
    status_code: int = 422
    detail: str = "Order parameters failed validation checks (e.g. invalid price)"

class RiskLimitViolation(TradingException):
    status_code: int = 403
    detail: str = "Pre-trade risk check failed (exposure limits violated)"

class InvalidOrderStatusException(TradingException):
    status_code: int = 400
    detail: str = "Requested operation is invalid for current order status"