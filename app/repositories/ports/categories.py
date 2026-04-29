from abc import ABC, abstractmethod
from models.categories import Attribute, Category, CategoryAttribute, PartCategoryLinks


class CategoryRepository(ABC):
    """
    Category Repository Interface Class
    """

    @abstractmethod
    async def add(self, category: Category) -> Category:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, category_id: int) -> Category | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_slug(self, slug: str) -> Category | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_key(self, key: str) -> Category | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_parent_id(self, parent_id: int | None) -> list[Category]:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list[Category]:
        raise NotImplementedError()


class AttributeRepository(ABC):
    """
    Attribute Repository Interface Class
    """

    @abstractmethod
    async def add(self, attribute: Attribute) -> Attribute:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, attribute_id: int) -> Attribute | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list[Attribute]:
        raise NotImplementedError()


class CategoryAttributeRepository(ABC):
    """
    CategoryAttribute Repository Interface Class
    """

    @abstractmethod
    async def add(self, category_attribute: CategoryAttribute) -> CategoryAttribute:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, category_attribute_id: int) -> CategoryAttribute | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_category_id(self, category_id: int) -> list[CategoryAttribute]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_attribute_id(self, attribute_id: int) -> list[CategoryAttribute]:
        raise NotImplementedError()


class PartCategoryLinksRepository(ABC):
    """
    PartCategoryLinks Repository Interface Class
    """

    @abstractmethod
    async def add(self, part_category_link: PartCategoryLinks) -> PartCategoryLinks:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, part_category_link_id: int) -> PartCategoryLinks | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_part_id(self, part_id: int) -> list[PartCategoryLinks]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_category_id(self, category_id: int) -> list[PartCategoryLinks]:
        raise NotImplementedError()

    @abstractmethod
    async def get_primary_category(self, part_id: int) -> PartCategoryLinks | None:
        raise NotImplementedError()
