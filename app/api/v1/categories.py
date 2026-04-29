from fastapi import APIRouter, status

from dependencies.categories import (
    CategoryServiceDep,
    AttributeServiceDep,
    CategoryAttributeServiceDep,
    PartCategoryLinksServiceDep,
)
from schemas.categories import (
    CategoryCreateRequest,
    CategoryResponse,
    AttributeCreateRequest,
    AttributeResponse,
    CategoryAttributeCreateRequest,
    CategoryAttributeResponse,
    PartCategoryLinksCreateRequest,
    PartCategoryLinksResponse,
)


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


# Category endpoints
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(
    category_info: CategoryCreateRequest,
    category_service: CategoryServiceDep,
) -> CategoryResponse:
    return await category_service.create_category(category_info)


@router.get("/{category_id}")
async def get_category(
    category_id: int,
    category_service: CategoryServiceDep,
) -> CategoryResponse:
    return await category_service.get_category_by_id(category_id)


@router.get("/slug/{slug}")
async def get_category_by_slug(
    slug: str,
    category_service: CategoryServiceDep,
) -> CategoryResponse:
    return await category_service.get_category_by_slug(slug)


@router.get("/parent/{parent_id}")
async def get_categories_by_parent_id(
    parent_id: int | None,
    category_service: CategoryServiceDep,
) -> list[CategoryResponse]:
    return await category_service.get_categories_by_parent_id(parent_id)


@router.get("/")
async def get_all_categories(
    category_service: CategoryServiceDep,
) -> list[CategoryResponse]:
    return await category_service.get_all_categories()


# Attribute endpoints
@router.post("/attributes", status_code=status.HTTP_201_CREATED)
async def create_attribute(
    attribute_info: AttributeCreateRequest,
    attribute_service: AttributeServiceDep,
) -> AttributeResponse:
    return await attribute_service.create_attribute(attribute_info)


@router.get("/attributes/{attribute_id}")
async def get_attribute(
    attribute_id: int,
    attribute_service: AttributeServiceDep,
) -> AttributeResponse:
    return await attribute_service.get_attribute_by_id(attribute_id)


@router.get("/attributes")
async def get_all_attributes(
    attribute_service: AttributeServiceDep,
) -> list[AttributeResponse]:
    return await attribute_service.get_all_attributes()


# CategoryAttribute endpoints
@router.post("/category-attributes", status_code=status.HTTP_201_CREATED)
async def create_category_attribute(
    category_attribute_info: CategoryAttributeCreateRequest,
    category_attribute_service: CategoryAttributeServiceDep,
) -> CategoryAttributeResponse:
    return await category_attribute_service.create_category_attribute(category_attribute_info)


@router.get("/{category_id}/attributes")
async def get_category_attributes_by_category_id(
    category_id: int,
    category_attribute_service: CategoryAttributeServiceDep,
) -> list[CategoryAttributeResponse]:
    return await category_attribute_service.get_category_attributes_by_category_id(category_id)


# PartCategoryLinks endpoints
@router.post("/part-category-links", status_code=status.HTTP_201_CREATED)
async def create_part_category_link(
    link_info: PartCategoryLinksCreateRequest,
    part_category_links_service: PartCategoryLinksServiceDep,
) -> PartCategoryLinksResponse:
    return await part_category_links_service.create_part_category_link(link_info)


@router.get("/parts/{part_id}/categories")
async def get_links_by_part_id(
    part_id: int,
    part_category_links_service: PartCategoryLinksServiceDep,
) -> list[PartCategoryLinksResponse]:
    return await part_category_links_service.get_links_by_part_id(part_id)


@router.get("/parts/{part_id}/primary-category")
async def get_primary_category(
    part_id: int,
    part_category_links_service: PartCategoryLinksServiceDep,
) -> PartCategoryLinksResponse:
    return await part_category_links_service.get_primary_category(part_id)
