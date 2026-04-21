from collections.abc import Callable

from models.example import Example
from repositories.example import ExampleRepository
from sqlalchemy.ext.asyncio import AsyncSession
from uow.ports import UnitOfWorkABC


class UnitOfWork(UnitOfWorkABC):
    def __init__(self, session_factory: Callable[[], AsyncSession]) -> None:
        self._session_factory = session_factory

    async def __aenter__(self):
        self._session = self._session_factory()
        self.examle = ExampleRepository(self._session, Example)

        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if exc_type:
            await self.rollback()
        else:
            await self._session.close()

    async def commit(self):
        try:
            await self._session.commit()
        except Exception:
            await self.rollback()
            raise

    async def rollback(self):
        try:
            await self._session.rollback()
        finally:
            await self._session.close()
