from typing import Annotated

from dependencies.uow import UowDependency
from fastapi import Depends

from services.ports import (
    ManufacturerServiceABC,
    CarModelServiceABC,
    CarModificationServiceABC,
)
from services.cars import (
    ManufacturerService,
    CarModelService,
    CarModificationService,
)


def get_manufacturer_service(uow: UowDependency) -> ManufacturerServiceABC:
    return ManufacturerService(uow)


ManufacturerServiceDep = Annotated[ManufacturerServiceABC, Depends(get_manufacturer_service)]


def get_car_model_service(uow: UowDependency) -> CarModelServiceABC:
    return CarModelService(uow)


CarModelServiceDep = Annotated[CarModelServiceABC, Depends(get_car_model_service)]


def get_car_modification_service(uow: UowDependency) -> CarModificationServiceABC:
    return CarModificationService(uow)


CarModificationServiceDep = Annotated[CarModificationServiceABC, Depends(get_car_modification_service)]
