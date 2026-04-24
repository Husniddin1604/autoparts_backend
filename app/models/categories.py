from models.base import Base
from sqlalchemy import Boolean, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Category(Base):
    __tablename__ = "categories"

    parent_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"), index=True, nullable=True)
    name_uz: Mapped[str] = mapped_column(String)
    name_ru: Mapped[str] = mapped_column(String)
    name_en: Mapped[str] = mapped_column(String)
    slug: Mapped[str] = mapped_column(String, unique=True)
    key: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String)
    sort_order: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    parent = relationship(
        "Category",
        remote_side="Category.id",
        back_populates="children"
    )

    children = relationship(
        "Category",
        back_populates="parent"
    )
    part_category_links = relationship("PartCategoryLinks", back_populates="category")
    category_attributes = relationship("CategoryAttribute", back_populates="category")


    __table_args__ = (
        UniqueConstraint("parent_id", "slug"),
    )

    def __repr__(self):
        return f"{self.key} {self.is_active}"


class PartCategoryLinks(Base):
    from models.autoparts import Part

    __tablename__ = "part_category_links"

    part_id: Mapped[int] = mapped_column(ForeignKey("parts.id"), index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), index=True)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False)

    part: Mapped[Part] = relationship("Part", back_populates="part_category_links")
    category: Mapped[Category] = relationship("Category", back_populates="part_category_links")


    __table_args__ = (
        UniqueConstraint("part_id", "category_id"),
    )

    def __repr__(self):
        return f"{self.part.name_en} {self.category.name_uz} {self.is_primary}"


class Attribute(Base):
    __tablename__ = "attributes"

    name_uz: Mapped[str] = mapped_column(String)
    name_ru: Mapped[str] = mapped_column(String)
    name_en: Mapped[str] = mapped_column(String)
    unit: Mapped[str] = mapped_column(String)
    data_type: Mapped[str] = mapped_column(String)

    category_attributes = relationship("CategoryAttribute", back_populates="attribute")
    product_attribute_values = relationship("ProductAttributeValues", back_populates="attribute")

    def __repr__(self):
        return self.name_en


class CategoryAttribute(Base):
    __tablename__ = "category_attributes"

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), index=True)
    attribute_id: Mapped[int] = mapped_column(ForeignKey("attributes.id"), index=True)
    is_filterable: Mapped[bool] = mapped_column(Boolean)
    is_required: Mapped[bool] = mapped_column(Boolean)

    category: Mapped[Category] = relationship("Category", back_populates="category_attributes")
    attribute: Mapped[Attribute] = relationship("Attribute", back_populates="category_attributes")


    __table_args__ = (
        UniqueConstraint("category_id", "attribute_id"),
    )

    def __repr__(self):
        return f"{self.category.name_en} {self.attribute.name_en}"

