class AlphaForgeException(Exception):
    """Base system exception for AlphaForge applications."""
    status_code: int = 500
    detail: str = "Internal server error"

    def __init__(self, detail: str | None = None) -> None:
        if detail:
            self.detail = detail
        super().__init__(self.detail)

# --- Authentication & Access Exceptions ---
class AuthenticationException(AlphaForgeException):
    status_code: int = 401
    detail: str = "Authentication failed"

class AuthorizationException(AlphaForgeException):
    status_code: int = 403
    detail: str = "Insufficient permissions"

# --- Database & Entity Exceptions ---
class EntityNotFoundException(AlphaForgeException):
    status_code: int = 404
    detail: str = "Requested resource was not found"

class DatabaseConflictException(AlphaForgeException):
    status_code: int = 409
    detail: str = "Conflict occurred during database transaction"

# --- Schema & Validation Exceptions ---
class SchemaValidationException(AlphaForgeException):
    status_code: int = 422
    detail: str = "Request parameters failed schema validation validation checks"