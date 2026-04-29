from fastapi import APIRouter

from dependencies.autoparts import (
    BrandServiceDep,
    PartServiceDep,
    PartNumbersServiceDep,
    CrossReferenceServiceDep,
    PartFitmentServiceDep,
)
from schemas.autoparts import (
    BrandResponse,
    PartResponse,
    PartNumbersResponse,
    CrossReferenceResponse,
    PartFitmentResponse,
)


router = APIRouter(
    prefix="/autoparts",
    tags=["shop-autoparts"],
)


# Brand endpoints (read-only)
@router.get("/brands/{brand_id}")
async def get_brand(
    brand_id: int,
    brand_service: BrandServiceDep,
) -> BrandResponse:
    return await brand_service.get_brand_by_id(brand_id)


@router.get("/brands")
async def get_all_brands(
    brand_service: BrandServiceDep,
) -> list[BrandResponse]:
    return await brand_service.get_all_brands()


# Part endpoints (read-only)
@router.get("/parts/{part_id}")
async def get_part(
    part_id: int,
    part_service: PartServiceDep,
) -> PartResponse:
    return await part_service.get_part_by_id(part_id)


@router.get("/parts/slug/{slug}")
async def get_part_by_slug(
    slug: str,
    part_service: PartServiceDep,
) -> PartResponse:
    return await part_service.get_part_by_slug(slug)


@router.get("/parts")
async def get_all_parts(
    part_service: PartServiceDep,
) -> list[PartResponse]:
    return await part_service.get_all_parts()


# PartNumbers endpoints (read-only)
@router.get("/part-numbers/{part_number_id}")
async def get_part_number(
    part_number_id: int,
    part_numbers_service: PartNumbersServiceDep,
) -> PartNumbersResponse:
    return await part_numbers_service.get_part_number_by_id(part_number_id)


@router.get("/parts/{part_id}/part-numbers")
async def get_part_numbers_by_part_id(
    part_id: int,
    part_numbers_service: PartNumbersServiceDep,
) -> list[PartNumbersResponse]:
    return await part_numbers_service.get_part_numbers_by_part_id(part_id)


# CrossReference endpoints (read-only)
@router.get("/part-numbers/{part_number_id}/cross-references")
async def get_cross_references_by_part_number_id(
    part_number_id: int,
    cross_reference_service: CrossReferenceServiceDep,
) -> list[CrossReferenceResponse]:
    return await cross_reference_service.get_cross_references_by_part_number_id(part_number_id)


# PartFitment endpoints (read-only)
@router.get("/parts/{part_id}/fitments")
async def get_fitments_by_part_id(
    part_id: int,
    part_fitment_service: PartFitmentServiceDep,
) -> list[PartFitmentResponse]:
    return await part_fitment_service.get_fitments_by_part_id(part_id)


@router.get("/car-modifications/{car_modification_id}/fitments")
async def get_fitments_by_car_modification_id(
    car_modification_id: int,
    part_fitment_service: PartFitmentServiceDep,
) -> list[PartFitmentResponse]:
    return await part_fitment_service.get_fitments_by_car_modification_id(car_modification_id)
