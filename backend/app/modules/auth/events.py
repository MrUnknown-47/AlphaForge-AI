# Event definitions and publishers for Auth operations

class UserRegisteredEvent:
    """Triggered immediately after a user record is committed to PostgreSQL."""
    def __init__(self, user_id: str, email: str):
        self.user_id = user_id
        self.email = email

class UserLoggedInEvent:
    """Triggered on successful password check and session generation."""
    def __init__(self, user_id: str, ip_address: str):
        self.user_id = user_id
        self.ip_address = ip_address

async def publish_user_registered(event: UserRegisteredEvent) -> None:
    # Publishing logic skeleton to alert systems
    pass

async def publish_user_logged_in(event: UserLoggedInEvent) -> None:
    # Audit log tracking publisher skeleton
    pass