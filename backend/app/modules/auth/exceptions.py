from app.shared.exceptions import AlphaForgeException

class AuthException(AlphaForgeException):
    status_code: int = 400
    detail: str = "Authentication error"

class UserAlreadyExistsException(AuthException):
    status_code: int = 409
    detail: str = "User with this email or username already exists"

class InvalidCredentialsException(AuthException):
    status_code: int = 401
    detail: str = "Incorrect email or password"

class SessionExpiredException(AuthException):
    status_code: int = 401
    detail: str = "Refresh session has expired"

class InvalidTokenException(AuthException):
    status_code: int = 401
    detail: str = "Provided authentication token is invalid or expired"

class UnauthorizedException(AuthException):
    status_code: int = 401
    detail: str = "Access token is missing or invalid"

class ForbiddenException(AuthException):
    status_code: int = 403
    detail: str = "Insufficient permissions to perform this operation"

class PasswordValidationException(AuthException):
    status_code: int = 400
    detail: str = "Password must be between 8 and 128 characters"