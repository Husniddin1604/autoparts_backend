from abc import ABC, abstractmethod
from repositories.ports.users import UserRepository
from repositories.ports.autoparts import (
    BrandRepository,
    PartRepository,
    PartNumbersRepository,
    CrossReferenceRepository,
    PartFitmentRepository,
)
from repositories.ports.cars import (
    ManufacturerRepository,
    CarModelRepository,
    CarModificationRepository,
)
from repositories.ports.categories import (
    CategoryRepository,
    AttributeRepository,
    CategoryAttributeRepository,
    PartCategoryLinksRepository,
)
from repositories.ports.products import (
    ProductRepository,
    StockRepository,
    ProductAttributeValuesRepository,
)


class UnitOfWorkABC(ABC):
    user: UserRepository
    brand: BrandRepository
    part: PartRepository
    part_numbers: PartNumbersRepository
    cross_reference: CrossReferenceRepository
    part_fitment: PartFitmentRepository
    manufacturer: ManufacturerRepository
    car_model: CarModelRepository
    car_modification: CarModificationRepository
    category: CategoryRepository
    attribute: AttributeRepository
    category_attribute: CategoryAttributeRepository
    part_category_links: PartCategoryLinksRepository
    product: ProductRepository
    stock: StockRepository
    product_attribute_values: ProductAttributeValuesRepository

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError()

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError()

    @abstractmethod
    async def commit(self):
        raise NotImplementedError()

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError()
