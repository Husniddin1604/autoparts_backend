from core.exceptions import BusinessException, CustomValidationException
from models.categories import Category, Attribute, CategoryAttribute, PartCategoryLinks
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
from services.ports import (
    CategoryServiceABC,
    AttributeServiceABC,
    CategoryAttributeServiceABC,
    PartCategoryLinksServiceABC,
)
from uow.ports import UnitOfWorkABC


class CategoryService(CategoryServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_category(self, category_info: CategoryCreateRequest) -> CategoryResponse:
        existing_category = await self.uow.category.get_by_key(category_info.key)
        if existing_category:
            raise CustomValidationException("Category with this key already exists")

        if category_info.parent_id:
            parent = await self.uow.category.get_by_id(category_info.parent_id)
            if not parent:
                raise BusinessException("Parent category not found")

        category = Category(**category_info.model_dump())
        created_category = await self.uow.category.add(category)
        return CategoryResponse.model_validate(created_category)

    async def get_category_by_id(self, category_id: int) -> CategoryResponse:
        category = await self.uow.category.get_by_id(category_id)
        if not category:
            raise BusinessException("Category not found")
        return CategoryResponse.model_validate(category)

    async def get_category_by_slug(self, slug: str) -> CategoryResponse:
        category = await self.uow.category.get_by_slug(slug)
        if not category:
            raise BusinessException("Category not found")
        return CategoryResponse.model_validate(category)

    async def get_categories_by_parent_id(self, parent_id: int | None) -> list[CategoryResponse]:
        categories = await self.uow.category.get_by_parent_id(parent_id)
        return [CategoryResponse.model_validate(c) for c in categories]

    async def get_all_categories(self) -> list[CategoryResponse]:
        categories = await self.uow.category.get_all()
        return [CategoryResponse.model_validate(c) for c in categories]


class AttributeService(AttributeServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_attribute(self, attribute_info: AttributeCreateRequest) -> AttributeResponse:
        attribute = Attribute(**attribute_info.model_dump())
        created_attribute = await self.uow.attribute.add(attribute)
        return AttributeResponse.model_validate(created_attribute)

    async def get_attribute_by_id(self, attribute_id: int) -> AttributeResponse:
        attribute = await self.uow.attribute.get_by_id(attribute_id)
        if not attribute:
            raise BusinessException("Attribute not found")
        return AttributeResponse.model_validate(attribute)

    async def get_all_attributes(self) -> list[AttributeResponse]:
        attributes = await self.uow.attribute.get_all()
        return [AttributeResponse.model_validate(a) for a in attributes]


class CategoryAttributeService(CategoryAttributeServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_category_attribute(self, category_attribute_info: CategoryAttributeCreateRequest) -> CategoryAttributeResponse:
        category = await self.uow.category.get_by_id(category_attribute_info.category_id)
        if not category:
            raise BusinessException("Category not found")

        attribute = await self.uow.attribute.get_by_id(category_attribute_info.attribute_id)
        if not attribute:
            raise BusinessException("Attribute not found")

        category_attribute = CategoryAttribute(**category_attribute_info.model_dump())
        created_category_attribute = await self.uow.category_attribute.add(category_attribute)
        return CategoryAttributeResponse.model_validate(created_category_attribute)

    async def get_category_attributes_by_category_id(self, category_id: int) -> list[CategoryAttributeResponse]:
        category_attributes = await self.uow.category_attribute.get_by_category_id(category_id)
        return [CategoryAttributeResponse.model_validate(ca) for ca in category_attributes]


class PartCategoryLinksService(PartCategoryLinksServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_part_category_link(self, link_info: PartCategoryLinksCreateRequest) -> PartCategoryLinksResponse:
        part = await self.uow.part.get_by_id(link_info.part_id)
        if not part:
            raise BusinessException("Part not found")

        category = await self.uow.category.get_by_id(link_info.category_id)
        if not category:
            raise BusinessException("Category not found")

        part_category_link = PartCategoryLinks(**link_info.model_dump())
        created_link = await self.uow.part_category_links.add(part_category_link)
        return PartCategoryLinksResponse.model_validate(created_link)

    async def get_links_by_part_id(self, part_id: int) -> list[PartCategoryLinksResponse]:
        links = await self.uow.part_category_links.get_by_part_id(part_id)
        return [PartCategoryLinksResponse.model_validate(l) for l in links]

    async def get_primary_category(self, part_id: int) -> PartCategoryLinksResponse:
        link = await self.uow.part_category_links.get_primary_category(part_id)
        if not link:
            raise BusinessException("Primary category not found for this part")
        return PartCategoryLinksResponse.model_validate(link)
