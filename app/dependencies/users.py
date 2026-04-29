import secrets
from typing import Annotated

from core.config import settings
from dependencies.uow import UowDependency
from dependencies.auth import AuthServiceDep
from fastapi import Depends, HTTPException, status
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
)
from models.users import User
from services.ports import UserServiceABC
from services.users import UserService


def get_user_service(uow: UowDependency) -> UserServiceABC:
    """
    Factory function to create an instance of UserService.
    """
    return UserService(uow)


UserServiceDep = Annotated[UserServiceABC, Depends(get_user_service)]


security = HTTPBearer()

async def get_request_user(
    auth_service: AuthServiceDep,
    user_service: UserServiceDep,
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> User:
    payload = await auth_service.verify_access_token(credentials.credentials)

    if payload is None or "user_uuid" not in payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_uuid = payload["user_uuid"]

    user = await user_service.get_user_by_uuid(user_uuid)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


RequestUserDep = Annotated[User, Depends(get_request_user)]


# basic_security = HTTPBasic()
#
# async def get_basic_auth_user(
#         credentials: HTTPBasicCredentials = Depends(basic_security)
# ) -> str:
#     correct_username = secrets.compare_digest(
#         credentials.username, settings.INTERNAL_USERNAME
#     )
#     correct_password = secrets.compare_digest(
#         credentials.password, settings.INTERNAL_PASSWORD
#     )
#     if not (correct_username and correct_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Basic"},
#         )
#     return credentials.username
#
#
# BasicAuthUserDep = Annotated[str, Depends(get_basic_auth_user)]
#
#
# async def get_integration_basic_auth_user(
#         credentials: HTTPBasicCredentials = Depends(basic_security),
# ) -> str:
#     for usernamePassword in settings.INTEGRATION_USERS.split(";"):
#         _username, _password = usernamePassword.split(":")
#         if credentials.username == _username and credentials.password == _password:
#             return credentials.username
#
#     raise HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Invalid authentication credentials",
#         headers={"WWW-Authenticate": "Basic"},
#     )
#
#
# IntegrationBasicAuthUserDep = Annotated[str, Depends(get_integration_basic_auth_user)]
