from fastapi import APIRouter, status

from dependencies.users import UserServiceDep
from schemas.users import UserCreateRequest, RegisterResponse


router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    user_info: UserCreateRequest,
    user_service: UserServiceDep,
) -> RegisterResponse:
    return await user_service.create_user(user_info)
