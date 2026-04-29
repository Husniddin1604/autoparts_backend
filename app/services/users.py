import logging

from core.config import settings
from core.exceptions import BusinessException, CustomValidationException
from core.security import create_access_token, create_refresh_token

from models.users import User
from schemas.users import (
    UserCreateRequest,
    UserInfoResponse,
    UserUpdateRequest,
    UserUpdateResponse,
    RegisterResponse,
)
from services.ports import UserServiceABC
from uow.ports import UnitOfWorkABC

logger = logging.getLogger(__name__)


class UserService(UserServiceABC):
    def __init__(
        self,
        uow: UnitOfWorkABC,
    ):
        self.uow = uow

    async def create_user(self, user_info: UserCreateRequest) -> RegisterResponse:
        """
        Create a user.
        :param user_info: User information.
        :return: Registration response with user info and tokens.
        """
        existUser = await self.uow.user.get_by_email(user_info.email)

        if existUser:
            raise CustomValidationException("User with this email already exists")

        # Create new user (your existing logic)
        user_model = User(**user_info.model_dump())
        user = await self.uow.user.add(user_model)

        # Generate tokens
        access_token = create_access_token(str(user.user_uuid), user.email)
        refresh_token = create_refresh_token(str(user.user_uuid), user.email)

        return RegisterResponse(
            user=UserInfoResponse.model_validate(user),
            access_token=access_token,
            refresh_token=refresh_token,
        )

    async def get_user_info(self, user_uuid: str) -> UserInfoResponse:
        """
        Get user information by user ID.
        :param user_uuid: The UUID of the user.
        :return: User information response.
        """
        user = await self.uow.user.get_by_uuid(user_uuid)
        return UserInfoResponse.model_validate(user)

    async def get_user_by_uuid(self, user_uuid: str) -> User:
        user = await self.uow.user.get_by_uuid(user_uuid)

        if not user:
            raise BusinessException("User not found")

        return user
