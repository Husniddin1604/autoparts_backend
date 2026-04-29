from fastapi import APIRouter, status

from dependencies.autoparts import (
    BrandServiceDep,
    PartServiceDep,
    PartNumbersServiceDep,
    CrossReferenceServiceDep,
    PartFitmentServiceDep,
)
from schemas.autoparts import (
    BrandCreateRequest,
    BrandResponse,
    PartCreateRequest,
    PartResponse,
    PartNumbersCreateRequest,
    PartNumbersResponse,
    CrossReferenceCreateRequest,
    CrossReferenceResponse,
    PartFitmentCreateRequest,
    PartFitmentResponse,
)


router = APIRouter(
    prefix="/autoparts",
    tags=["autoparts"],
)


# Brand endpoints
@router.post("/brands", status_code=status.HTTP_201_CREATED)
async def create_brand(
    brand_info: BrandCreateRequest,
    brand_service: BrandServiceDep,
) -> BrandResponse:
    return await brand_service.create_brand(brand_info)


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


# Part endpoints
@router.post("/parts", status_code=status.HTTP_201_CREATED)
async def create_part(
    part_info: PartCreateRequest,
    part_service: PartServiceDep,
) -> PartResponse:
    return await part_service.create_part(part_info)


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


# PartNumbers endpoints
@router.post("/part-numbers", status_code=status.HTTP_201_CREATED)
async def create_part_number(
    part_number_info: PartNumbersCreateRequest,
    part_numbers_service: PartNumbersServiceDep,
) -> PartNumbersResponse:
    return await part_numbers_service.create_part_number(part_number_info)


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


# CrossReference endpoints
@router.post("/cross-references", status_code=status.HTTP_201_CREATED)
async def create_cross_reference(
    cross_ref_info: CrossReferenceCreateRequest,
    cross_reference_service: CrossReferenceServiceDep,
) -> CrossReferenceResponse:
    return await cross_reference_service.create_cross_reference(cross_ref_info)


@router.get("/part-numbers/{part_number_id}/cross-references")
async def get_cross_references_by_part_number_id(
    part_number_id: int,
    cross_reference_service: CrossReferenceServiceDep,
) -> list[CrossReferenceResponse]:
    return await cross_reference_service.get_cross_references_by_part_number_id(part_number_id)


# PartFitment endpoints
@router.post("/part-fitments", status_code=status.HTTP_201_CREATED)
async def create_part_fitment(
    fitment_info: PartFitmentCreateRequest,
    part_fitment_service: PartFitmentServiceDep,
) -> PartFitmentResponse:
    return await part_fitment_service.create_part_fitment(fitment_info)


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
