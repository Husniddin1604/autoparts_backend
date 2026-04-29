from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.autoparts import Brand, CrossReference, Part, PartFitment, PartNumbers
from repositories.ports.autoparts import (
    BrandRepository,
    PartRepository,
    PartNumbersRepository,
    CrossReferenceRepository,
    PartFitmentRepository,
)


def _filter_deleted(query, model):
    """Helper to filter out soft-deleted records."""
    return query.where(model.deleted_at.is_(None))


class SqlAlchemyBrandRepository(BrandRepository):
    """
    Brand Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, brand: Brand) -> Brand:
        self.session.add(brand)
        await self.session.flush()
        await self.session.refresh(brand)
        return brand

    async def get_by_id(self, brand_id: int) -> Brand | None:
        result = await self.session.execute(
            _filter_deleted(select(Brand).where(Brand.id == brand_id), Brand)
        )
        return result.scalar_one_or_none()

    async def get_by_name(self, name: str) -> Brand | None:
        result = await self.session.execute(
            _filter_deleted(select(Brand).where(Brand.name == name), Brand)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Brand]:
        result = await self.session.execute(_filter_deleted(select(Brand), Brand))
        return list(result.scalars().all())


class SqlAlchemyPartRepository(PartRepository):
    """
    Part Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, part: Part) -> Part:
        self.session.add(part)
        await self.session.flush()
        await self.session.refresh(part)
        return part

    async def get_by_id(self, part_id: int) -> Part | None:
        result = await self.session.execute(
            _filter_deleted(select(Part).where(Part.id == part_id), Part)
        )
        return result.scalar_one_or_none()

    async def get_by_slug(self, slug: str) -> Part | None:
        result = await self.session.execute(
            _filter_deleted(select(Part).where(Part.slug == slug), Part)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Part]:
        result = await self.session.execute(_filter_deleted(select(Part), Part))
        return list(result.scalars().all())


class SqlAlchemyPartNumbersRepository(PartNumbersRepository):
    """
    PartNumbers Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, part_number: PartNumbers) -> PartNumbers:
        self.session.add(part_number)
        await self.session.flush()
        await self.session.refresh(part_number)
        return part_number

    async def get_by_id(self, part_number_id: int) -> PartNumbers | None:
        result = await self.session.execute(
            _filter_deleted(select(PartNumbers).where(PartNumbers.id == part_number_id), PartNumbers)
        )
        return result.scalar_one_or_none()

    async def get_by_number(self, number: str) -> PartNumbers | None:
        result = await self.session.execute(
            _filter_deleted(select(PartNumbers).where(PartNumbers.number == number), PartNumbers)
        )
        return result.scalar_one_or_none()

    async def get_by_part_id(self, part_id: int) -> list[PartNumbers]:
        result = await self.session.execute(
            _filter_deleted(select(PartNumbers).where(PartNumbers.part_id == part_id), PartNumbers)
        )
        return list(result.scalars().all())

    async def get_by_brand_id(self, brand_id: int) -> list[PartNumbers]:
        result = await self.session.execute(
            _filter_deleted(select(PartNumbers).where(PartNumbers.brand_id == brand_id), PartNumbers)
        )
        return list(result.scalars().all())


class SqlAlchemyCrossReferenceRepository(CrossReferenceRepository):
    """
    CrossReference Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, cross_ref: CrossReference) -> CrossReference:
        self.session.add(cross_ref)
        await self.session.flush()
        await self.session.refresh(cross_ref)
        return cross_ref

    async def get_by_id(self, cross_ref_id: int) -> CrossReference | None:
        result = await self.session.execute(
            _filter_deleted(select(CrossReference).where(CrossReference.id == cross_ref_id), CrossReference)
        )
        return result.scalar_one_or_none()

    async def get_by_part_number_id(self, part_number_id: int) -> list[CrossReference]:
        result = await self.session.execute(
            _filter_deleted(select(CrossReference).where(CrossReference.part_number_id == part_number_id), CrossReference)
        )
        return list(result.scalars().all())

    async def get_cross_refs(self, part_number_id: int) -> list[PartNumbers]:
        result = await self.session.execute(
            _filter_deleted(
                select(PartNumbers)
                .join(CrossReference, CrossReference.cross_part_number_id == PartNumbers.id)
                .where(CrossReference.part_number_id == part_number_id),
                PartNumbers
            )
        )
        return list(result.scalars().all())


class SqlAlchemyPartFitmentRepository(PartFitmentRepository):
    """
    PartFitment Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, part_fitment: PartFitment) -> PartFitment:
        self.session.add(part_fitment)
        await self.session.flush()
        await self.session.refresh(part_fitment)
        return part_fitment

    async def get_by_id(self, fitment_id: int) -> PartFitment | None:
        result = await self.session.execute(
            _filter_deleted(select(PartFitment).where(PartFitment.id == fitment_id), PartFitment)
        )
        return result.scalar_one_or_none()

    async def get_by_part_id(self, part_id: int) -> list[PartFitment]:
        result = await self.session.execute(
            _filter_deleted(select(PartFitment).where(PartFitment.part_id == part_id), PartFitment)
        )
        return list(result.scalars().all())

    async def get_by_car_modification_id(self, car_modification_id: int) -> list[PartFitment]:
        result = await self.session.execute(
            _filter_deleted(select(PartFitment).where(PartFitment.car_modification_id == car_modification_id), PartFitment)
        )
        return list(result.scalars().all())
