from core.exceptions import BusinessException, CustomValidationException
from models.products import Product, Stock, ProductAttributeValues
from schemas.products import (
    ProductCreateRequest,
    ProductResponse,
    StockCreateRequest,
    StockResponse,
    ProductAttributeValuesCreateRequest,
    ProductAttributeValuesResponse,
)
from services.ports import (
    ProductServiceABC,
    StockServiceABC,
    ProductAttributeValuesServiceABC,
)
from uow.ports import UnitOfWorkABC


class ProductService(ProductServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_product(self, product_info: ProductCreateRequest) -> ProductResponse:
        existing_product = await self.uow.product.get_by_barcode(product_info.barcode)
        if existing_product:
            raise CustomValidationException("Product with this barcode already exists")

        part_number = await self.uow.part_numbers.get_by_id(product_info.part_number_id)
        if not part_number:
            raise BusinessException("Part number not found")

        product = Product(**product_info.model_dump())
        created_product = await self.uow.product.add(product)
        return ProductResponse.model_validate(created_product)

    async def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = await self.uow.product.get_by_id(product_id)
        if not product:
            raise BusinessException("Product not found")
        return ProductResponse.model_validate(product)

    async def get_product_by_barcode(self, barcode: str) -> ProductResponse:
        product = await self.uow.product.get_by_barcode(barcode)
        if not product:
            raise BusinessException("Product not found")
        return ProductResponse.model_validate(product)

    async def get_products_by_part_number_id(self, part_number_id: int) -> list[ProductResponse]:
        products = await self.uow.product.get_by_part_number_id(part_number_id)
        return [ProductResponse.model_validate(p) for p in products]


class StockService(StockServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_stock(self, stock_info: StockCreateRequest) -> StockResponse:
        product = await self.uow.product.get_by_id(stock_info.product_id)
        if not product:
            raise BusinessException("Product not found")

        stock = Stock(**stock_info.model_dump())
        created_stock = await self.uow.stock.add(stock)
        return StockResponse.model_validate(created_stock)

    async def get_stock_by_id(self, stock_id: int) -> StockResponse:
        stock = await self.uow.stock.get_by_id(stock_id)
        if not stock:
            raise BusinessException("Stock not found")
        return StockResponse.model_validate(stock)

    async def get_stocks_by_product_id(self, product_id: int) -> list[StockResponse]:
        stocks = await self.uow.stock.get_by_product_id(product_id)
        return [StockResponse.model_validate(s) for s in stocks]

    async def update_stock_quantity(self, stock_id: int, quantity: int) -> StockResponse:
        stock = await self.uow.stock.get_by_id(stock_id)
        if not stock:
            raise BusinessException("Stock not found")

        updated_stock = await self.uow.stock.update_quantity(stock_id, quantity)
        return StockResponse.model_validate(updated_stock)

    async def update_stock_reserved_quantity(self, stock_id: int, reserved_quantity: int) -> StockResponse:
        stock = await self.uow.stock.get_by_id(stock_id)
        if not stock:
            raise BusinessException("Stock not found")

        updated_stock = await self.uow.stock.update_reserved_quantity(stock_id, reserved_quantity)
        return StockResponse.model_validate(updated_stock)


class ProductAttributeValuesService(ProductAttributeValuesServiceABC):
    def __init__(self, uow: UnitOfWorkABC):
        self.uow = uow

    async def create_product_attribute_value(self, attribute_value_info: ProductAttributeValuesCreateRequest) -> ProductAttributeValuesResponse:
        product = await self.uow.product.get_by_id(attribute_value_info.product_id)
        if not product:
            raise BusinessException("Product not found")

        attribute = await self.uow.attribute.get_by_id(attribute_value_info.attribute_id)
        if not attribute:
            raise BusinessException("Attribute not found")

        existing_value = await self.uow.product_attribute_values.get_by_product_and_attribute(
            attribute_value_info.product_id,
            attribute_value_info.attribute_id
        )
        if existing_value:
            raise CustomValidationException("Attribute value already exists for this product")

        product_attribute_value = ProductAttributeValues(**attribute_value_info.model_dump())
        created_value = await self.uow.product_attribute_values.add(product_attribute_value)
        return ProductAttributeValuesResponse.model_validate(created_value)

    async def get_attribute_values_by_product_id(self, product_id: int) -> list[ProductAttributeValuesResponse]:
        attribute_values = await self.uow.product_attribute_values.get_by_product_id(product_id)
        return [ProductAttributeValuesResponse.model_validate(av) for av in attribute_values]
