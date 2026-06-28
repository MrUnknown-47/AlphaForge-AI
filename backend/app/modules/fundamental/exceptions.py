from app.shared.exceptions import AlphaForgeException

class FundamentalException(AlphaForgeException):
    """Base custom exception for the Fundamental domain."""
    status_code: int = 400
    detail: str = "Fundamental data operations error"

class StatementNotFoundException(FundamentalException):
    status_code: int = 404
    detail: str = "Financial statements not found for target ticker"