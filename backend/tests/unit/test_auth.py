import pytest
from app.modules.security.auth_manager import AuthManager

def test_auth_hashing_and_tokens():
    manager = AuthManager()
    
    pw = "securepass123"
    hashed = manager.hash_password(pw)
    assert hashed != pw
    assert manager.verify_password(pw, hashed) is True
    assert manager.verify_password("wrongpass", hashed) is False

    tokens = manager.generate_tokens("user1", "TRADER")
    assert "access_token" in tokens
    assert "refresh_token" in tokens

    # Token Revocation
    manager.revoke_token(tokens["access_token"])
    assert manager.is_token_revoked(tokens["access_token"]) is True