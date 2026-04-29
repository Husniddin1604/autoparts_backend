from core.exceptions import BusinessException, CustomValidationException
from models.autoparts import Brand, Part, PartNumbers, CrossReference, PartFitment
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
from services.ports import (
    BrandServiceABC,
    PartServiceABC,
    PartNumbersServiceABC,
    CrossReferenceServiceABC,
    PartFitmentServiceABC,
)
from uow.ports import UnitOfWorkABC


class BrandService(BrandServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_brand(self, brand_info: BrandCreateRequest) -> BrandResponse:
        existing_brand = await self.uow.brand.get_by_name(brand_info.name)
        if existing_brand:
            raise CustomValidationException("Brand with this name already exists")

        brand = Brand(**brand_info.model_dump())
        created_brand = await self.uow.brand.add(brand)
        return BrandResponse.model_validate(created_brand)

    async def get_brand_by_id(self, brand_id: int) -> BrandResponse:
        brand = await self.uow.brand.get_by_id(brand_id)
        if not brand:
            raise BusinessException("Brand not found")
        return BrandResponse.model_validate(brand)

    async def get_all_brands(self) -> list[BrandResponse]:
        brands = await self.uow.brand.get_all()
        return [BrandResponse.model_validate(brand) for brand in brands]


class PartService(PartServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_part(self, part_info: PartCreateRequest) -> PartResponse:
        existing_part = await self.uow.part.get_by_slug(part_info.slug)
        if existing_part:
            raise CustomValidationException("Part with this slug already exists")

        part = Part(**part_info.model_dump())
        created_part = await self.uow.part.add(part)
        return PartResponse.model_validate(created_part)

    async def get_part_by_id(self, part_id: int) -> PartResponse:
        part = await self.uow.part.get_by_id(part_id)
        if not part:
            raise BusinessException("Part not found")
        return PartResponse.model_validate(part)

    async def get_part_by_slug(self, slug: str) -> PartResponse:
        part = await self.uow.part.get_by_slug(slug)
        if not part:
            raise BusinessException("Part not found")
        return PartResponse.model_validate(part)

    async def get_all_parts(self) -> list[PartResponse]:
        parts = await self.uow.part.get_all()
        return [PartResponse.model_validate(part) for part in parts]


class PartNumbersService(PartNumbersServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_part_number(self, part_number_info: PartNumbersCreateRequest) -> PartNumbersResponse:
        part = await self.uow.part.get_by_id(part_number_info.part_id)
        if not part:
            raise BusinessException("Part not found")

        brand = await self.uow.brand.get_by_id(part_number_info.brand_id)
        if not brand:
            raise BusinessException("Brand not found")

        part_number = PartNumbers(**part_number_info.model_dump())
        created_part_number = await self.uow.part_numbers.add(part_number)
        return PartNumbersResponse.model_validate(created_part_number)

    async def get_part_number_by_id(self, part_number_id: int) -> PartNumbersResponse:
        part_number = await self.uow.part_numbers.get_by_id(part_number_id)
        if not part_number:
            raise BusinessException("Part number not found")
        return PartNumbersResponse.model_validate(part_number)

    async def get_part_numbers_by_part_id(self, part_id: int) -> list[PartNumbersResponse]:
        part_numbers = await self.uow.part_numbers.get_by_part_id(part_id)
        return [PartNumbersResponse.model_validate(pn) for pn in part_numbers]


class CrossReferenceService(CrossReferenceServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_cross_reference(self, cross_ref_info: CrossReferenceCreateRequest) -> CrossReferenceResponse:
        part_number = await self.uow.part_numbers.get_by_id(cross_ref_info.part_number_id)
        if not part_number:
            raise BusinessException("Part number not found")

        cross_part_number = await self.uow.part_numbers.get_by_id(cross_ref_info.cross_part_number_id)
        if not cross_part_number:
            raise BusinessException("Cross part number not found")

        cross_ref = CrossReference(**cross_ref_info.model_dump())
        created_cross_ref = await self.uow.cross_reference.add(cross_ref)
        return CrossReferenceResponse.model_validate(created_cross_ref)

    async def get_cross_references_by_part_number_id(self, part_number_id: int) -> list[CrossReferenceResponse]:
        cross_refs = await self.uow.cross_reference.get_by_part_number_id(part_number_id)
        return [CrossReferenceResponse.model_validate(cr) for cr in cross_refs]


class PartFitmentService(PartFitmentServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_part_fitment(self, fitment_info: PartFitmentCreateRequest) -> PartFitmentResponse:
        part = await self.uow.part.get_by_id(fitment_info.part_id)
        if not part:
            raise BusinessException("Part not found")

        car_modification = await self.uow.car_modification.get_by_id(fitment_info.car_modification_id)
        if not car_modification:
            raise BusinessException("Car modification not found")

        fitment = PartFitment(**fitment_info.model_dump())
        created_fitment = await self.uow.part_fitment.add(fitment)
        return PartFitmentResponse.model_validate(created_fitment)

    async def get_fitments_by_part_id(self, part_id: int) -> list[PartFitmentResponse]:
        fitments = await self.uow.part_fitment.get_by_part_id(part_id)
        return [PartFitmentResponse.model_validate(f) for f in fitments]

    async def get_fitments_by_car_modification_id(self, car_modification_id: int) -> list[PartFitmentResponse]:
        fitments = await self.uow.part_fitment.get_by_car_modification_id(car_modification_id)
        return [PartFitmentResponse.model_validate(f) for f in fitments]
