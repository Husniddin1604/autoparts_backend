from abc import ABC, abstractmethod
from models.products import Product, ProductAttributeValues, Stock


class ProductRepository(ABC):
    """
    Product Repository Interface Class
    """

    @abstractmethod
    async def add(self, product: Product) -> Product:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, product_id: int) -> Product | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_barcode(self, barcode: str) -> Product | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_part_number_id(self, part_number_id: int) -> list[Product]:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list[Product]:
        raise NotImplementedError()


class StockRepository(ABC):
    """
    Stock Repository Interface Class
    """

    @abstractmethod
    async def add(self, stock: Stock) -> Stock:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, stock_id: int) -> Stock | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_product_id(self, product_id: int) -> list[Stock]:
        raise NotImplementedError()

    @abstractmethod
    async def update_quantity(self, stock_id: int, quantity: int) -> Stock:
        raise NotImplementedError()

    @abstractmethod
    async def update_reserved_quantity(self, stock_id: int, reserved_quantity: int) -> Stock:
        raise NotImplementedError()


class ProductAttributeValuesRepository(ABC):
    """
    ProductAttributeValues Repository Interface Class
    """

    @abstractmethod
    async def add(self, product_attribute_value: ProductAttributeValues) -> ProductAttributeValues:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, product_attribute_value_id: int) -> ProductAttributeValues | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_product_id(self, product_id: int) -> list[ProductAttributeValues]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_attribute_id(self, attribute_id: int) -> list[ProductAttributeValues]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_product_and_attribute(self, product_id: int, attribute_id: int) -> ProductAttributeValues | None:
        raise NotImplementedError()
