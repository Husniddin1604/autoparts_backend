from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.cars import CarModel, CarModification, Manufacturer
from repositories.ports.cars import (
    ManufacturerRepository,
    CarModelRepository,
    CarModificationRepository,
)


class SqlAlchemyManufacturerRepository(ManufacturerRepository):
    """
    Manufacturer Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, manufacturer: Manufacturer) -> Manufacturer:
        self.session.add(manufacturer)
        await self.session.flush()
        await self.session.refresh(manufacturer)
        return manufacturer

    async def get_by_id(self, manufacturer_id: int) -> Manufacturer | None:
        result = await self.session.execute(
            select(Manufacturer).where(Manufacturer.id == manufacturer_id)
        )
        return result.scalar_one_or_none()

    async def get_by_name(self, name: str) -> Manufacturer | None:
        result = await self.session.execute(
            select(Manufacturer).where(Manufacturer.name == name)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Manufacturer]:
        result = await self.session.execute(select(Manufacturer))
        return list(result.scalars().all())


class SqlAlchemyCarModelRepository(CarModelRepository):
    """
    CarModel Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, car_model: CarModel) -> CarModel:
        self.session.add(car_model)
        await self.session.flush()
        await self.session.refresh(car_model)
        return car_model

    async def get_by_id(self, car_model_id: int) -> CarModel | None:
        result = await self.session.execute(
            select(CarModel).where(CarModel.id == car_model_id)
        )
        return result.scalar_one_or_none()

    async def get_by_manufacturer_id(self, manufacturer_id: int) -> list[CarModel]:
        result = await self.session.execute(
            select(CarModel).where(CarModel.manufacturer_id == manufacturer_id)
        )
        return list(result.scalars().all())

    async def get_all(self) -> list[CarModel]:
        result = await self.session.execute(select(CarModel))
        return list(result.scalars().all())


class SqlAlchemyCarModificationRepository(CarModificationRepository):
    """
    CarModification Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, car_modification: CarModification) -> CarModification:
        self.session.add(car_modification)
        await self.session.flush()
        await self.session.refresh(car_modification)
        return car_modification

    async def get_by_id(self, car_modification_id: int) -> CarModification | None:
        result = await self.session.execute(
            select(CarModification).where(CarModification.id == car_modification_id)
        )
        return result.scalar_one_or_none()

    async def get_by_model_id(self, model_id: int) -> list[CarModification]:
        result = await self.session.execute(
            select(CarModification).where(CarModification.model_id == model_id)
        )
        return list(result.scalars().all())

    async def get_by_engine_code(self, engine_code: str) -> list[CarModification]:
        result = await self.session.execute(
            select(CarModification).where(CarModification.engine_code == engine_code)
        )
        return list(result.scalars().all())
