import hmac
import hashlib
import base64
import json
import time
from typing import Dict, Any, Optional

class JWTManager:
    def __init__(self, secret: str = "supersecretkey") -> None:
        self.secret = secret.encode()
        self.revoked_tokens = set()

    def _base64url_encode(self, data: bytes) -> str:
        return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")

    def _base64url_decode(self, data: str) -> bytes:
        padding = 4 - (len(data) % 4)
        return base64.urlsafe_b64decode(data + "=" * padding)

    def create_token(self, payload: Dict[str, Any], expiry_seconds: int) -> str:
        header = {"alg": "HS256", "typ": "JWT"}
        payload_copy = payload.copy()
        payload_copy["exp"] = int(time.time()) + expiry_seconds

        header_b64 = self._base64url_encode(json.dumps(header).encode())
        payload_b64 = self._base64url_encode(json.dumps(payload_copy).encode())

        message = f"{header_b64}.{payload_b64}".encode()
        sig = hmac.new(self.secret, message, hashlib.sha256).digest()
        sig_b64 = self._base64url_encode(sig)

        return f"{header_b64}.{payload_b64}.{sig_b64}"

    def decode_token(self, token: str) -> Optional[Dict[str, Any]]:
        if token in self.revoked_tokens:
            return None
        try:
            parts = token.split(".")
            if len(parts) != 3:
                return None

            header_b64, payload_b64, sig_b64 = parts
            message = f"{header_b64}.{payload_b64}".encode()
            
            # Verify signature
            expected_sig = hmac.new(self.secret, message, hashlib.sha256).digest()
            expected_sig_b64 = self._base64url_encode(expected_sig)
            
            if not hmac.compare_digest(sig_b64, expected_sig_b64):
                return None

            payload = json.loads(self._base64url_decode(payload_b64).decode())
            
            # Check expiry
            if payload.get("exp", 0) < time.time():
                return None

            return payload
        except Exception:
            return None

    def create_access_token(self, payload: Dict[str, Any]) -> str:
        return self.create_token(payload, 900)

    def create_refresh_token(self, payload: Dict[str, Any]) -> str:
        return self.create_token(payload, 604800)

    def verify_access_token(self, token: str) -> Optional[Dict[str, Any]]:
        return self.decode_token(token)

    def verify_refresh_token(self, token: str) -> Optional[Dict[str, Any]]:
        return self.decode_token(token)

    def revoke_token(self, token: str) -> None:
        self.revoked_tokens.add(token)
