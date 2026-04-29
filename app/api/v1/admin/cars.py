from fastapi import APIRouter, status

from dependencies.cars import (
    ManufacturerServiceDep,
    CarModelServiceDep,
    CarModificationServiceDep,
)
from schemas.cars import (
    ManufacturerCreateRequest,
    ManufacturerResponse,
    CarModelCreateRequest,
    CarModelResponse,
    CarModificationCreateRequest,
    CarModificationResponse,
)


router = APIRouter(
    prefix="/cars",
    tags=["admin-cars"],
)


# Manufacturer endpoints (write operations)
@router.post("/manufacturers", status_code=status.HTTP_201_CREATED)
async def create_manufacturer(
    manufacturer_info: ManufacturerCreateRequest,
    manufacturer_service: ManufacturerServiceDep,
) -> ManufacturerResponse:
    return await manufacturer_service.create_manufacturer(manufacturer_info)


@router.get("/manufacturers/{manufacturer_id}")
async def get_manufacturer(
    manufacturer_id: int,
    manufacturer_service: ManufacturerServiceDep,
) -> ManufacturerResponse:
    return await manufacturer_service.get_manufacturer_by_id(manufacturer_id)


@router.get("/manufacturers")
async def get_all_manufacturers(
    manufacturer_service: ManufacturerServiceDep,
) -> list[ManufacturerResponse]:
    return await manufacturer_service.get_all_manufacturers()


# CarModel endpoints (write operations)
@router.post("/models", status_code=status.HTTP_201_CREATED)
async def create_car_model(
    car_model_info: CarModelCreateRequest,
    car_model_service: CarModelServiceDep,
) -> CarModelResponse:
    return await car_model_service.create_car_model(car_model_info)


@router.get("/models/{car_model_id}")
async def get_car_model(
    car_model_id: int,
    car_model_service: CarModelServiceDep,
) -> CarModelResponse:
    return await car_model_service.get_car_model_by_id(car_model_id)


@router.get("/manufacturers/{manufacturer_id}/models")
async def get_car_models_by_manufacturer_id(
    manufacturer_id: int,
    car_model_service: CarModelServiceDep,
) -> list[CarModelResponse]:
    return await car_model_service.get_car_models_by_manufacturer_id(manufacturer_id)


# CarModification endpoints (write operations)
@router.post("/modifications", status_code=status.HTTP_201_CREATED)
async def create_car_modification(
    modification_info: CarModificationCreateRequest,
    car_modification_service: CarModificationServiceDep,
) -> CarModificationResponse:
    return await car_modification_service.create_car_modification(modification_info)


@router.get("/modifications/{modification_id}")
async def get_car_modification(
    modification_id: int,
    car_modification_service: CarModificationServiceDep,
) -> CarModificationResponse:
    return await car_modification_service.get_car_modification_by_id(modification_id)


@router.get("/models/{model_id}/modifications")
async def get_modifications_by_model_id(
    model_id: int,
    car_modification_service: CarModificationServiceDep,
) -> list[CarModificationResponse]:
    return await car_modification_service.get_modifications_by_model_id(model_id)
