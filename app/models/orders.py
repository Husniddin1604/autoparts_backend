from models.base import Base
from sqlalchemy import Date, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship

from decimal import Decimal


class Order(Base):
    __tablename__ = "orders"

    customer_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    status: Mapped[str] = mapped_column(String)
    total_price: Mapped[Decimal] = mapped_column(DECIMAL)

    customer = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[Decimal] = mapped_column(DECIMAL)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")
