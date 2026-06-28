import os
import hmac
import hashlib
from typing import Dict, Any, Optional, Set
from app.modules.security.jwt_manager import JWTManager

class AuthManager:
    def __init__(self, secret: str = "supersecretkey") -> None:
        self.jwt = JWTManager(secret)
        self.revoked_tokens: Set[str] = set()

    def hash_password(self, password: str) -> str:
        salt = os.urandom(16)
        pw_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
        return f"pbkdf2_sha256$100000${salt.hex()}${pw_hash.hex()}"

    def verify_password(self, password: str, hashed: str) -> bool:
        try:
            parts = hashed.split("$")
            if len(parts) != 4 or parts[0] != "pbkdf2_sha256":
                return False
            iterations = int(parts[1])
            salt = bytes.fromhex(parts[2])
            expected_hash = bytes.fromhex(parts[3])
            actual_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations)
            return hmac.compare_digest(actual_hash, expected_hash)
        except Exception:
            return False

    def generate_tokens(self, username: str, role: str) -> Dict[str, str]:
        payload = {"sub": username, "role": role}
        # access_token: 15 minutes = 900 seconds
        # refresh_token: 7 days = 604800 seconds
        return {
            "access_token": self.jwt.create_token(payload, 900),
            "refresh_token": self.jwt.create_token(payload, 604800)
        }

    def revoke_token(self, token: str) -> None:
        self.revoked_tokens.add(token)

    def is_token_revoked(self, token: str) -> bool:
        return token in self.revoked_tokens
