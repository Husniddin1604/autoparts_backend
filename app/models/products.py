from decimal import Decimal

from models.base import Base
from sqlalchemy import (DECIMAL, CheckConstraint, ForeignKey, Integer, String,
                        UniqueConstraint)
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Product(Base):
    __tablename__ = "products"

    part_number_id: Mapped[int] = mapped_column(ForeignKey("part_numbers.id"), index=True)
    name: Mapped[str] = mapped_column(String)
    selling_price: Mapped[Decimal] = mapped_column(DECIMAL, nullable=False)
    barcode: Mapped[str] = mapped_column(String, unique=True, index=True)

    part_number = relationship("PartNumbers", back_populates="products")
    product_attribute_values = relationship("ProductAttributeValues", back_populates="product")
    stocks = relationship("Stock", back_populates="product")

    def __repr__(self):
        return self.name


class Stock(Base):
    __tablename__ = "stocks"

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    quantity: Mapped[int] = mapped_column(Integer, default=0)
    reserved_quantity: Mapped[int] = mapped_column(Integer, default=0)
    purchase_price: Mapped[Decimal] = mapped_column(DECIMAL)

    product = relationship("Product", back_populates="stocks")

    __table_args__ = (
        CheckConstraint("quantity >= 0"),
        CheckConstraint("reserved_quantity >= 0"),
    )

    def __repr__(self):
        return f"{self.product.name} {self.quantity}"


class ProductAttributeValues(Base):
    __tablename__ = "product_attribute_values"

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    attribute_id: Mapped[int] = mapped_column(ForeignKey("attributes.id"), index=True)
    value_text: Mapped[str | None] = mapped_column(String, nullable=True)
    value_number: Mapped[Decimal | None] = mapped_column(DECIMAL, nullable=True)

    product = relationship("Product", back_populates="product_attribute_values")
    attribute = relationship("Attribute", back_populates="product_attribute_values")


    __table_args__ = (
        UniqueConstraint("product_id", "attribute_id"),
    )

    def __repr__(self):
        return f"{self.product.name} {self.attribute.name_en}"