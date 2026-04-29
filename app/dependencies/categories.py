from typing import Annotated

from dependencies.uow import UowDependency
from fastapi import Depends

from services.ports import (
    CategoryServiceABC,
    AttributeServiceABC,
    CategoryAttributeServiceABC,
    PartCategoryLinksServiceABC,
)
from services.categories import (
    CategoryService,
    AttributeService,
    CategoryAttributeService,
    PartCategoryLinksService,
)


def get_category_service(uow: UowDependency) -> CategoryServiceABC:
    return CategoryService(uow)


CategoryServiceDep = Annotated[CategoryServiceABC, Depends(get_category_service)]


def get_attribute_service(uow: UowDependency) -> AttributeServiceABC:
    return AttributeService(uow)


AttributeServiceDep = Annotated[AttributeServiceABC, Depends(get_attribute_service)]


def get_category_attribute_service(uow: UowDependency) -> CategoryAttributeServiceABC:
    return CategoryAttributeService(uow)


CategoryAttributeServiceDep = Annotated[CategoryAttributeServiceABC, Depends(get_category_attribute_service)]


def get_part_category_links_service(uow: UowDependency) -> PartCategoryLinksServiceABC:
    return PartCategoryLinksService(uow)


PartCategoryLinksServiceDep = Annotated[PartCategoryLinksServiceABC, Depends(get_part_category_links_service)]
