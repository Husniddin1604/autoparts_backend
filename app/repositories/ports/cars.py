from abc import ABC, abstractmethod
from models.cars import CarModel, CarModification, Manufacturer


class ManufacturerRepository(ABC):
    """
    Manufacturer Repository Interface Class
    """

    @abstractmethod
    async def add(self, manufacturer: Manufacturer) -> Manufacturer:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, manufacturer_id: int) -> Manufacturer | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_name(self, name: str) -> Manufacturer | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list[Manufacturer]:
        raise NotImplementedError()


class CarModelRepository(ABC):
    """
    CarModel Repository Interface Class
    """

    @abstractmethod
    async def add(self, car_model: CarModel) -> CarModel:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, car_model_id: int) -> CarModel | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_manufacturer_id(self, manufacturer_id: int) -> list[CarModel]:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list[CarModel]:
        raise NotImplementedError()


class CarModificationRepository(ABC):
    """
    CarModification Repository Interface Class
    """

    @abstractmethod
    async def add(self, car_modification: CarModification) -> CarModification:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, car_modification_id: int) -> CarModification | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_model_id(self, model_id: int) -> list[CarModification]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_engine_code(self, engine_code: str) -> list[CarModification]:
        raise NotImplementedError()
