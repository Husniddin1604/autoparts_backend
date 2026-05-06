from pydantic import BaseModel, ConfigDict
from datetime import datetime
from uuid import UUID


class UserBaseSchema(BaseModel):
    """Base schema for user data."""

    username: str
    first_name: str
    last_name: str
    middle_name: str | None
    email: str
    phone: str | None

    model_config = ConfigDict(from_attributes=True)


class UserCreateRequest(UserBaseSchema):
    """Schema for creating a new user."""
    password: str


class UserUpdateRequest(UserBaseSchema):
    """Schema for updating user information."""
    is_staff: bool
    is_active: bool
    user_uuid: UUID


class UserUpdateResponse(UserBaseSchema):
    """Schema for updating user information."""
    is_staff: bool
    is_active: bool
    user_uuid: UUID


class UserInfoResponse(UserBaseSchema):
    """Schema for user information response."""
    is_staff: bool
    is_active: bool
    created_at: datetime
    user_uuid: UUID


class RegisterResponse(BaseModel):
    """Schema for registration response with tokens."""
    user: UserInfoResponse
    access_token: str
    refresh_token: str