from fastapi import APIRouter, Depends, status, Response, Cookie, HTTPException
from app.config import settings
from app.modules.auth.schemas import (
    UserCreate,
    UserLogin,
    UserResponse,
    TokenResponse,
    PasswordResetRequest,
    PasswordResetConfirm,
    EmailVerificationConfirm,
    RefreshRequest,
)
from app.modules.auth.facade import AuthFacade
from app.modules.auth.dependencies import get_auth_facade

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(data: UserCreate, facade: AuthFacade = Depends(get_auth_facade)):
    return await facade.register_user(data)

@router.post("/login", response_model=TokenResponse)
async def login(
    data: UserLogin,
    response: Response,
    facade: AuthFacade = Depends(get_auth_facade)
):
    tokens = await facade.authenticate_user(data)
    # Set Refresh Token in Secure Cookie
    response.set_cookie(
        key="refresh_token",
        value=tokens.refresh_token,
        httponly=True,
        secure=settings.ENVIRONMENT == "production",
        samesite="lax",
        max_age=60*60*24*7,
        path="/"
    )
    return tokens

@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(
    response: Response,
    refresh_token: str | None = Cookie(None),
    facade: AuthFacade = Depends(get_auth_facade)
):
    if refresh_token:
        await facade.logout_user(refresh_token)
    response.delete_cookie("refresh_token")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post("/refresh", response_model=TokenResponse)
async def refresh(
    data: RefreshRequest | None = None,
    refresh_token: str | None = Cookie(None),
    facade: AuthFacade = Depends(get_auth_facade)
):
    token = refresh_token or (data.refresh_token if data else "")
    if not token:
        raise HTTPException(status_code=401, detail="Missing refresh token")
    return await facade.refresh_session(token)

@router.post("/verify-email", status_code=status.HTTP_200_OK)
async def verify_email(data: EmailVerificationConfirm, facade: AuthFacade = Depends(get_auth_facade)):
    # Email verification routing skeleton
    return {"message": "Email verified successfully"}

@router.post("/reset-password", status_code=status.HTTP_200_OK)
async def reset_password_request(data: PasswordResetRequest, facade: AuthFacade = Depends(get_auth_facade)):
    # Password reset requesting logic skeleton
    return {"message": "Password reset email sent if address exists"}

@router.post("/reset-password/confirm", status_code=status.HTTP_200_OK)
async def reset_password_confirm(data: PasswordResetConfirm, facade: AuthFacade = Depends(get_auth_facade)):
    # Reset completion logic skeleton
    return {"message": "Password reset completed successfully"}