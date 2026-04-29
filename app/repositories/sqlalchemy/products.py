from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, update

from models.products import Product, ProductAttributeValues, Stock
from repositories.ports.products import (
    ProductRepository,
    StockRepository,
    ProductAttributeValuesRepository,
)


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

    async def get_by_id(self, product_id: int) -> Product | None:
        result = await self.session.execute(
            select(Product).where(Product.id == product_id)
        )
        return result.scalar_one_or_none()

    async def get_by_barcode(self, barcode: str) -> Product | None:
        result = await self.session.execute(
            select(Product).where(Product.barcode == barcode)
        )
        return result.scalar_one_or_none()

    async def get_by_part_number_id(self, part_number_id: int) -> list[Product]:
        result = await self.session.execute(
            select(Product).where(Product.part_number_id == part_number_id)
        )
        return list(result.scalars().all())

    async def get_all(self) -> list[Product]:
        result = await self.session.execute(select(Product))
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

    async def get_by_id(self, stock_id: int) -> Stock | None:
        result = await self.session.execute(
            select(Stock).where(Stock.id == stock_id)
        )
        return result.scalar_one_or_none()

    async def get_by_product_id(self, product_id: int) -> list[Stock]:
        result = await self.session.execute(
            select(Stock).where(Stock.product_id == product_id)
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

    async def get_by_id(self, product_attribute_value_id: int) -> ProductAttributeValues | None:
        result = await self.session.execute(
            select(ProductAttributeValues).where(ProductAttributeValues.id == product_attribute_value_id)
        )
        return result.scalar_one_or_none()

    async def get_by_product_id(self, product_id: int) -> list[ProductAttributeValues]:
        result = await self.session.execute(
            select(ProductAttributeValues).where(ProductAttributeValues.product_id == product_id)
        )
        return list(result.scalars().all())

    async def get_by_attribute_id(self, attribute_id: int) -> list[ProductAttributeValues]:
        result = await self.session.execute(
            select(ProductAttributeValues).where(ProductAttributeValues.attribute_id == attribute_id)
        )
        return list(result.scalars().all())

    async def get_by_product_and_attribute(self, product_id: int, attribute_id: int) -> ProductAttributeValues | None:
        result = await self.session.execute(
            select(ProductAttributeValues).where(
                and_(
                    ProductAttributeValues.product_id == product_id,
                    ProductAttributeValues.attribute_id == attribute_id
                )
            )
        )
        return result.scalar_one_or_none()
