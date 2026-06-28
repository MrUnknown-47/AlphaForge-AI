from app.shared.exceptions import AlphaForgeException

class PortfolioException(AlphaForgeException):
    status_code: int = 400
    detail: str = "Portfolio operations error"

class PortfolioNotFoundException(PortfolioException):
    status_code: int = 404
    detail: str = "Portfolio could not be found"

class InsufficientCashException(PortfolioException):
    status_code: int = 400
    detail: str = "Insufficient cash balance to execute withdraw or trade"

class InvalidTransactionException(PortfolioException):
    status_code: int = 400
    detail: str = "Invalid cash movement transaction requested"