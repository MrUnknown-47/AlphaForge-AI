# Celery tasks stub for auth module operations

def send_verification_email(email: str, token: str) -> None:
    """
    Background worker task to dispatch email verification codes to users.
    """
    pass

def send_password_reset_email(email: str, token: str) -> None:
    """
    Background worker task to dispatch password reset links to users.
    """
    pass