from typing import Annotated

from fastapi import Depends

from dependencies.uow import UowDependency

from services.ports import AuthServiceABC
from services.auth import AuthService


def get_auth_service(uow: UowDependency) -> AuthServiceABC:
    return AuthService(uow)

AuthServiceDep = Annotated[AuthServiceABC, Depends(get_auth_service)]