from collections.abc import Callable

from repositories.sqlalchemy.users import SqlAlchemyUserRepository
from repositories.sqlalchemy.autoparts import (
    SqlAlchemyBrandRepository,
    SqlAlchemyPartRepository,
    SqlAlchemyPartNumbersRepository,
    SqlAlchemyCrossReferenceRepository,
    SqlAlchemyPartFitmentRepository,
)
from repositories.sqlalchemy.cars import (
    SqlAlchemyManufacturerRepository,
    SqlAlchemyCarModelRepository,
    SqlAlchemyCarModificationRepository,
)
from repositories.sqlalchemy.categories import (
    SqlAlchemyCategoryRepository,
    SqlAlchemyAttributeRepository,
    SqlAlchemyCategoryAttributeRepository,
    SqlAlchemyPartCategoryLinksRepository,
)
from repositories.sqlalchemy.products import (
    SqlAlchemyProductRepository,
    SqlAlchemyStockRepository,
    SqlAlchemyProductAttributeValuesRepository,
)
from sqlalchemy.ext.asyncio import AsyncSession
from uow.ports import UnitOfWorkABC


class UnitOfWork(UnitOfWorkABC):
    def __init__(self, session_factory: Callable[[], AsyncSession]) -> None:
        self._session_factory = session_factory

    async def __aenter__(self):
        self._session = self._session_factory()
        self.user = SqlAlchemyUserRepository(self._session)
        self.brand = SqlAlchemyBrandRepository(self._session)
        self.part = SqlAlchemyPartRepository(self._session)
        self.part_numbers = SqlAlchemyPartNumbersRepository(self._session)
        self.cross_reference = SqlAlchemyCrossReferenceRepository(self._session)
        self.part_fitment = SqlAlchemyPartFitmentRepository(self._session)
        self.manufacturer = SqlAlchemyManufacturerRepository(self._session)
        self.car_model = SqlAlchemyCarModelRepository(self._session)
        self.car_modification = SqlAlchemyCarModificationRepository(self._session)
        self.category = SqlAlchemyCategoryRepository(self._session)
        self.attribute = SqlAlchemyAttributeRepository(self._session)
        self.category_attribute = SqlAlchemyCategoryAttributeRepository(self._session)
        self.part_category_links = SqlAlchemyPartCategoryLinksRepository(self._session)
        self.product = SqlAlchemyProductRepository(self._session)
        self.stock = SqlAlchemyStockRepository(self._session)
        self.product_attribute_values = SqlAlchemyProductAttributeValuesRepository(self._session)

        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        try:
            if exc_type:
                await self._session.rollback()
            else:
                await self._session.commit()
        finally:
            await self._session.close()

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
