from dependencies.users import RequestUserDep
from dependencies.auth import AuthServiceDep
from schemas.auth import LoginWithEmailRequest, LoginWithUsernameRequest
from fastapi import APIRouter, Depends
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

@router.post(
    "/logout",
)
async def logout_route(
    current_user: RequestUserDep,
    auth_service: AuthServiceDep,
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
):
    token = credentials.credentials
    return await auth_service.logout(token)

@router.post("/refresh-token")
async def refresh_token_route(
    current_user: RequestUserDep,
    auth_service: AuthServiceDep,
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
):
    token = credentials.credentials
    return await auth_service.refresh_token(token)
