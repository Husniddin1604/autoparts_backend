from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.users import User
from repositories.ports.users import UserRepository
from repositories.sqlalchemy import _filter_deleted


class SqlAlchemyUserRepository(UserRepository):
    """
    User Repository Class
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, user: User) -> User:
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)
        return user

    async def get_by_uuid(self, user_uuid: str) -> User | None:
        result = await self.session.execute(
            _filter_deleted(select(User).where(User.user_uuid == user_uuid), User)
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(
            _filter_deleted(select(User).where(User.email == email), User)
        )
        return result.scalar_one_or_none()

    async def get_by_username(self, username: str) -> User | None:
        result = await self.session.execute(
            _filter_deleted(select(User).where(User.username == username), User)
        )
        return result.scalar_one_or_none()

