from abc import ABC, abstractmethod
from models.users import User


class UserRepository(ABC):
    """
    User Repository Interface Class
    This class defines the interface for user repository operations.
    """

    @abstractmethod
    async def add(self, user: User) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_uuid(self, user_uuid: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_username(self, username: str) -> User | None:
        raise NotImplementedError()


