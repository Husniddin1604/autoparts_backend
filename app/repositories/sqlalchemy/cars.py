from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.cars import CarModel, CarModification, Manufacturer
from repositories.ports.cars import (
    ManufacturerRepository,
    CarModelRepository,
    CarModificationRepository,
)
from repositories.sqlalchemy import _filter_deleted


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

    async def add_many(self, manufacturers: list[Manufacturer]) -> list[Manufacturer]:
        self.session.add_all(manufacturers)
        await self.session.flush()
        await self.session.refresh(manufacturers)
        return manufacturers

    async def get_by_id(self, manufacturer_id: int) -> Manufacturer | None:
        result = await self.session.execute(
            _filter_deleted(select(Manufacturer).where(Manufacturer.id == manufacturer_id), Manufacturer)
        )
        return result.scalar_one_or_none()

    async def get_by_name(self, name: str) -> Manufacturer | None:
        result = await self.session.execute(
            _filter_deleted(select(Manufacturer).where(Manufacturer.name == name), Manufacturer)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Manufacturer]:
        result = await self.session.execute(_filter_deleted(select(Manufacturer), Manufacturer))
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

    async def add_many(self, car_models: list[CarModel]) -> list[CarModel]:
        self.session.add_all(car_models)
        await self.session.flush()
        await self.session.refresh(car_models)
        return car_models

    async def get_by_id(self, car_model_id: int) -> CarModel | None:
        result = await self.session.execute(
            _filter_deleted(select(CarModel).where(CarModel.id == car_model_id), CarModel)
        )
        return result.scalar_one_or_none()

    async def get_by_manufacturer_id(self, manufacturer_id: int) -> list[CarModel]:
        result = await self.session.execute(
            _filter_deleted(select(CarModel).where(CarModel.manufacturer_id == manufacturer_id), CarModel)
        )
        return list(result.scalars().all())

    async def get_all(self) -> list[CarModel]:
        result = await self.session.execute(_filter_deleted(select(CarModel), CarModel))
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

    async def add_many(self, car_modifications: list[CarModification]) -> list[CarModification]:
        self.session.add_all(car_modifications)
        await self.session.flush()
        await self.session.refresh(car_modifications)
        return car_modifications

    async def get_by_id(self, car_modification_id: int) -> CarModification | None:
        result = await self.session.execute(
            _filter_deleted(select(CarModification).where(CarModification.id == car_modification_id), CarModification)
        )
        return result.scalar_one_or_none()

    async def get_by_model_id(self, model_id: int) -> list[CarModification]:
        result = await self.session.execute(
            _filter_deleted(select(CarModification).where(CarModification.model_id == model_id), CarModification)
        )
        return list(result.scalars().all())

    async def get_by_engine_code(self, engine_code: str) -> list[CarModification]:
        result = await self.session.execute(
            _filter_deleted(select(CarModification).where(CarModification.engine_code == engine_code), CarModification)
        )
        return list(result.scalars().all())
