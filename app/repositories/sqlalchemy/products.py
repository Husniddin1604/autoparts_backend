from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, update

from models.products import Product, ProductAttributeValues, Stock
from repositories.ports.products import (
    ProductRepository,
    StockRepository,
    ProductAttributeValuesRepository,
)
from repositories.sqlalchemy import _filter_deleted


class SqlAlchemyProductRepository(ProductRepository):
    """
    Product Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, product: Product) -> Product:
        self.session.add(product)
        await self.session.flush()
        await self.session.refresh(product)
        return product

    async def add_many(self, products: list[Product]) -> list[Product]:
        self.session.add_all(products)
        await self.session.flush()
        await self.session.refresh(products)
        return products

    async def get_by_id(self, product_id: int) -> Product | None:
        result = await self.session.execute(
            _filter_deleted(select(Product).where(Product.id == product_id), Product)
        )
        return result.scalar_one_or_none()

    async def get_by_barcode(self, barcode: str) -> Product | None:
        result = await self.session.execute(
            _filter_deleted(select(Product).where(Product.barcode == barcode), Product)
        )
        return result.scalar_one_or_none()

    async def get_by_part_number_id(self, part_number_id: int) -> list[Product]:
        result = await self.session.execute(
            _filter_deleted(select(Product).where(Product.part_number_id == part_number_id), Product)
        )
        return list(result.scalars().all())

    async def get_all(self) -> list[Product]:
        result = await self.session.execute(_filter_deleted(select(Product), Product))
        return list(result.scalars().all())


class SqlAlchemyStockRepository(StockRepository):
    """
    Stock Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, stock: Stock) -> Stock:
        self.session.add(stock)
        await self.session.flush()
        await self.session.refresh(stock)
        return stock

    async def add_many(self, stocks: list[Stock]) -> list[Stock]:
        self.session.add_all(stocks)
        await self.session.flush()
        await self.session.refresh(stocks)
        return stocks

    async def get_by_id(self, stock_id: int) -> Stock | None:
        result = await self.session.execute(
            _filter_deleted(select(Stock).where(Stock.id == stock_id), Stock)
        )
        return result.scalar_one_or_none()

    async def get_by_product_id(self, product_id: int) -> list[Stock]:
        result = await self.session.execute(
            _filter_deleted(select(Stock).where(Stock.product_id == product_id), Stock)
        )
        return list(result.scalars().all())

    async def update_quantity(self, stock_id: int, quantity: int) -> Stock:
        await self.session.execute(
            update(Stock).where(Stock.id == stock_id).values(quantity=quantity)
        )
        await self.session.flush()
        return await self.get_by_id(stock_id)

    async def update_reserved_quantity(self, stock_id: int, reserved_quantity: int) -> Stock:
        await self.session.execute(
            update(Stock).where(Stock.id == stock_id).values(reserved_quantity=reserved_quantity)
        )
        await self.session.flush()
        return await self.get_by_id(stock_id)


class SqlAlchemyProductAttributeValuesRepository(ProductAttributeValuesRepository):
    """
    ProductAttributeValues Repository Implementation
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, product_attribute_value: ProductAttributeValues) -> ProductAttributeValues:
        self.session.add(product_attribute_value)
        await self.session.flush()
        await self.session.refresh(product_attribute_value)
        return product_attribute_value

    async def add_many(self, product_attribute_values: list[ProductAttributeValues]) -> list[ProductAttributeValues]:
        self.session.add_all(product_attribute_values)
        await self.session.flush()
        await self.session.refresh(product_attribute_values)
        return product_attribute_values

    async def get_by_id(self, product_attribute_value_id: int) -> ProductAttributeValues | None:
        result = await self.session.execute(
            _filter_deleted(select(ProductAttributeValues).where(ProductAttributeValues.id == product_attribute_value_id), ProductAttributeValues)
        )
        return result.scalar_one_or_none()

    async def get_by_product_id(self, product_id: int) -> list[ProductAttributeValues]:
        result = await self.session.execute(
            _filter_deleted(select(ProductAttributeValues).where(ProductAttributeValues.product_id == product_id), ProductAttributeValues)
        )
        return list(result.scalars().all())

    async def get_by_attribute_id(self, attribute_id: int) -> list[ProductAttributeValues]:
        result = await self.session.execute(
            _filter_deleted(select(ProductAttributeValues).where(ProductAttributeValues.attribute_id == attribute_id), ProductAttributeValues)
        )
        return list(result.scalars().all())

    async def get_by_product_and_attribute(self, product_id: int, attribute_id: int) -> ProductAttributeValues | None:
        result = await self.session.execute(
            _filter_deleted(
                select(ProductAttributeValues).where(
                    and_(
                        ProductAttributeValues.product_id == product_id,
                        ProductAttributeValues.attribute_id == attribute_id
                    )
                ),
                ProductAttributeValues
            )
        )
        return result.scalar_one_or_none()
