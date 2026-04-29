from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_

from models.categories import Attribute, Category, CategoryAttribute, PartCategoryLinks
from repositories.ports.categories import (
    CategoryRepository,
    AttributeRepository,
    CategoryAttributeRepository,
    PartCategoryLinksRepository,
)


def _filter_deleted(query, model):
    """Helper to filter out soft-deleted records."""
    return query.where(model.deleted_at.is_(None))


class SqlAlchemyCategoryRepository(CategoryRepository):
    """
    Category Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, category: Category) -> Category:
        self.session.add(category)
        await self.session.flush()
        await self.session.refresh(category)
        return category

    async def get_by_id(self, category_id: int) -> Category | None:
        result = await self.session.execute(
            _filter_deleted(select(Category).where(Category.id == category_id), Category)
        )
        return result.scalar_one_or_none()

    async def get_by_slug(self, slug: str) -> Category | None:
        result = await self.session.execute(
            _filter_deleted(select(Category).where(Category.slug == slug), Category)
        )
        return result.scalar_one_or_none()

    async def get_by_key(self, key: str) -> Category | None:
        result = await self.session.execute(
            _filter_deleted(select(Category).where(Category.key == key), Category)
        )
        return result.scalar_one_or_none()

    async def get_by_parent_id(self, parent_id: int | None) -> list[Category]:
        if parent_id is None:
            result = await self.session.execute(
                _filter_deleted(select(Category).where(Category.parent_id.is_(None)), Category)
            )
        else:
            result = await self.session.execute(
                _filter_deleted(select(Category).where(Category.parent_id == parent_id), Category)
            )
        return list(result.scalars().all())

    async def get_all(self) -> list[Category]:
        result = await self.session.execute(_filter_deleted(select(Category), Category))
        return list(result.scalars().all())


class SqlAlchemyAttributeRepository(AttributeRepository):
    """
    Attribute Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, attribute: Attribute) -> Attribute:
        self.session.add(attribute)
        await self.session.flush()
        await self.session.refresh(attribute)
        return attribute

    async def get_by_id(self, attribute_id: int) -> Attribute | None:
        result = await self.session.execute(
            _filter_deleted(select(Attribute).where(Attribute.id == attribute_id), Attribute)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Attribute]:
        result = await self.session.execute(_filter_deleted(select(Attribute), Attribute))
        return list(result.scalars().all())


class SqlAlchemyCategoryAttributeRepository(CategoryAttributeRepository):
    """
    CategoryAttribute Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, category_attribute: CategoryAttribute) -> CategoryAttribute:
        self.session.add(category_attribute)
        await self.session.flush()
        await self.session.refresh(category_attribute)
        return category_attribute

    async def get_by_id(self, category_attribute_id: int) -> CategoryAttribute | None:
        result = await self.session.execute(
            _filter_deleted(select(CategoryAttribute).where(CategoryAttribute.id == category_attribute_id), CategoryAttribute)
        )
        return result.scalar_one_or_none()

    async def get_by_category_id(self, category_id: int) -> list[CategoryAttribute]:
        result = await self.session.execute(
            _filter_deleted(select(CategoryAttribute).where(CategoryAttribute.category_id == category_id), CategoryAttribute)
        )
        return list(result.scalars().all())

    async def get_by_attribute_id(self, attribute_id: int) -> list[CategoryAttribute]:
        result = await self.session.execute(
            _filter_deleted(select(CategoryAttribute).where(CategoryAttribute.attribute_id == attribute_id), CategoryAttribute)
        )
        return list(result.scalars().all())


class SqlAlchemyPartCategoryLinksRepository(PartCategoryLinksRepository):
    """
    PartCategoryLinks Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, part_category_link: PartCategoryLinks) -> PartCategoryLinks:
        self.session.add(part_category_link)
        await self.session.flush()
        await self.session.refresh(part_category_link)
        return part_category_link

    async def get_by_id(self, part_category_link_id: int) -> PartCategoryLinks | None:
        result = await self.session.execute(
            _filter_deleted(select(PartCategoryLinks).where(PartCategoryLinks.id == part_category_link_id), PartCategoryLinks)
        )
        return result.scalar_one_or_none()

    async def get_by_part_id(self, part_id: int) -> list[PartCategoryLinks]:
        result = await self.session.execute(
            _filter_deleted(select(PartCategoryLinks).where(PartCategoryLinks.part_id == part_id), PartCategoryLinks)
        )
        return list(result.scalars().all())

    async def get_by_category_id(self, category_id: int) -> list[PartCategoryLinks]:
        result = await self.session.execute(
            _filter_deleted(select(PartCategoryLinks).where(PartCategoryLinks.category_id == category_id), PartCategoryLinks)
        )
        return list(result.scalars().all())

    async def get_primary_category(self, part_id: int) -> PartCategoryLinks | None:
        result = await self.session.execute(
            _filter_deleted(
                select(PartCategoryLinks).where(
                    and_(PartCategoryLinks.part_id == part_id, PartCategoryLinks.is_primary == True)
                ),
                PartCategoryLinks
            )
        )
        return result.scalar_one_or_none()
