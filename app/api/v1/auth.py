from typing import Optional

from dependencies.users import RequestUserDep, UserServiceDep
from dependencies.auth import AuthServiceDep
from schemas.auth import LoginWithEmailRequest, LoginWithUsernameRequest
from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)
bearer_scheme = HTTPBearer()


@router.post("/login/email")
async def login_with_email(
        credentials: LoginWithEmailRequest,
        auth_service: AuthServiceDep
) -> dict:
    return await auth_service.login_with_email(credentials.email, credentials.password)

@router.post("/login/username")
async def login_with_username(
        credentials: LoginWithUsernameRequest,
        auth_service: AuthServiceDep
) -> dict:
    return await auth_service.login_with_username(credentials.username, credentials.password)

@router.get(
    "/logout",
)
async def logout_route(
    current_user: RequestUserDep,
    auth_service: AuthServiceDep,
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
):
    token = credentials.credentials
    return await auth_service.logout(token)
