from typing import Annotated

from dependencies.uow import UowDependency
from fastapi import Depends

from services.ports import (
    BrandServiceABC,
    PartServiceABC,
    PartNumbersServiceABC,
    CrossReferenceServiceABC,
    PartFitmentServiceABC,
)
from services.autoparts import (
    BrandService,
    PartService,
    PartNumbersService,
    CrossReferenceService,
    PartFitmentService,
)


def get_brand_service(uow: UowDependency) -> BrandServiceABC:
    return BrandService(uow)


BrandServiceDep = Annotated[BrandServiceABC, Depends(get_brand_service)]


def get_part_service(uow: UowDependency) -> PartServiceABC:
    return PartService(uow)


PartServiceDep = Annotated[PartServiceABC, Depends(get_part_service)]


def get_part_numbers_service(uow: UowDependency) -> PartNumbersServiceABC:
    return PartNumbersService(uow)


PartNumbersServiceDep = Annotated[PartNumbersServiceABC, Depends(get_part_numbers_service)]


def get_cross_reference_service(uow: UowDependency) -> CrossReferenceServiceABC:
    return CrossReferenceService(uow)


CrossReferenceServiceDep = Annotated[CrossReferenceServiceABC, Depends(get_cross_reference_service)]


def get_part_fitment_service(uow: UowDependency) -> PartFitmentServiceABC:
    return PartFitmentService(uow)


PartFitmentServiceDep = Annotated[PartFitmentServiceABC, Depends(get_part_fitment_service)]
