from core.exceptions import BusinessException, CustomValidationException
from models.cars import Manufacturer, CarModel, CarModification
from schemas.cars import (
    ManufacturerCreateRequest,
    ManufacturerResponse,
    CarModelCreateRequest,
    CarModelResponse,
    CarModificationCreateRequest,
    CarModificationResponse,
)
from services.ports import (
    ManufacturerServiceABC,
    CarModelServiceABC,
    CarModificationServiceABC,
)
from uow.ports import UnitOfWorkABC


class ManufacturerService(ManufacturerServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_manufacturer(self, manufacturer_info: ManufacturerCreateRequest) -> ManufacturerResponse:
        existing_manufacturer = await self.uow.manufacturer.get_by_name(manufacturer_info.name)
        if existing_manufacturer:
            raise CustomValidationException("Manufacturer with this name already exists")

        manufacturer = Manufacturer(**manufacturer_info.model_dump())
        created_manufacturer = await self.uow.manufacturer.add(manufacturer)
        return ManufacturerResponse.model_validate(created_manufacturer)

    async def get_manufacturer_by_id(self, manufacturer_id: int) -> ManufacturerResponse:
        manufacturer = await self.uow.manufacturer.get_by_id(manufacturer_id)
        if not manufacturer:
            raise BusinessException("Manufacturer not found")
        return ManufacturerResponse.model_validate(manufacturer)

    async def get_all_manufacturers(self) -> list[ManufacturerResponse]:
        manufacturers = await self.uow.manufacturer.get_all()
        return [ManufacturerResponse.model_validate(m) for m in manufacturers]


class CarModelService(CarModelServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_car_model(self, car_model_info: CarModelCreateRequest) -> CarModelResponse:
        manufacturer = await self.uow.manufacturer.get_by_id(car_model_info.manufacturer_id)
        if not manufacturer:
            raise BusinessException("Manufacturer not found")

        car_model = CarModel(**car_model_info.model_dump())
        created_car_model = await self.uow.car_model.add(car_model)
        return CarModelResponse.model_validate(created_car_model)

    async def get_car_model_by_id(self, car_model_id: int) -> CarModelResponse:
        car_model = await self.uow.car_model.get_by_id(car_model_id)
        if not car_model:
            raise BusinessException("Car model not found")
        return CarModelResponse.model_validate(car_model)

    async def get_car_models_by_manufacturer_id(self, manufacturer_id: int) -> list[CarModelResponse]:
        car_models = await self.uow.car_model.get_by_manufacturer_id(manufacturer_id)
        return [CarModelResponse.model_validate(cm) for cm in car_models]


class CarModificationService(CarModificationServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_car_modification(self, modification_info: CarModificationCreateRequest) -> CarModificationResponse:
        car_model = await self.uow.car_model.get_by_id(modification_info.model_id)
        if not car_model:
            raise BusinessException("Car model not found")

        modification = CarModification(**modification_info.model_dump())
        created_modification = await self.uow.car_modification.add(modification)
        return CarModificationResponse.model_validate(created_modification)

    async def get_car_modification_by_id(self, modification_id: int) -> CarModificationResponse:
        modification = await self.uow.car_modification.get_by_id(modification_id)
        if not modification:
            raise BusinessException("Car modification not found")
        return CarModificationResponse.model_validate(modification)

    async def get_modifications_by_model_id(self, model_id: int) -> list[CarModificationResponse]:
        modifications = await self.uow.car_modification.get_by_model_id(model_id)
        return [CarModificationResponse.model_validate(m) for m in modifications]
