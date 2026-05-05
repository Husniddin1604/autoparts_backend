from models.base import Base
from sqlalchemy import Boolean, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Part(Base):
    __tablename__ = "parts"

    name_uz: Mapped[str] = mapped_column(String)
    name_ru: Mapped[str] = mapped_column(String)
    name_en: Mapped[str] = mapped_column(String)
    slug: Mapped[str] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String)

    part_category_links = relationship("PartCategoryLinks", back_populates="part")
    part_numbers = relationship("PartNumbers", back_populates="part")
    part_fitments = relationship("PartFitment", back_populates="part")

    def __repr__(self):
        return self.name_en


class Brand(Base):
    __tablename__ = "brands"

    name: Mapped[str] = mapped_column(String, unique=True)
    country = mapped_column(String, nullable=True)
    is_oem: Mapped[bool] = mapped_column(Boolean)

    part_numbers = relationship("PartNumbers", back_populates="brand")

    def __repr__(self):
        return self.name


class PartNumbers(Base):
    __tablename__ = "part_numbers"

    part_id: Mapped[int] = mapped_column(ForeignKey("parts.id"), index=True)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"), index=True)
    number: Mapped[str] = mapped_column(String, index=True)
    is_oem: Mapped[bool] = mapped_column(Boolean)
    replaced_by_id: Mapped[int | None] = mapped_column(
        ForeignKey("part_numbers.id"),
        index=True,
        nullable=True
    )

    replaced_by = relationship(
        "PartNumbers",
        foreign_keys=[replaced_by_id],
        remote_side="PartNumbers.id",
        back_populates="replaces"
    )

    replaces = relationship(
        "PartNumbers",
        foreign_keys=[replaced_by_id],
        back_populates="replaced_by"
    )
    cross_refs_from = relationship(
        "CrossReference",
        foreign_keys="CrossReference.part_number_id",
        back_populates="part_number"
    )
    cross_refs_to = relationship(
        "CrossReference",
        foreign_keys="CrossReference.cross_part_number_id",
        back_populates="cross_part_number"
    )
    part = relationship("Part", back_populates="part_numbers")
    brand = relationship("Brand", back_populates="part_numbers")
    products = relationship("Product", back_populates="part_number")


    __table_args__ = (
        UniqueConstraint("brand_id", "number"),
    )

    def __repr__(self):
        return self.number


class CrossReference(Base):
    __tablename__ = "cross_references"

    part_number_id: Mapped[int] = mapped_column(ForeignKey("part_numbers.id"), index=True)
    cross_part_number_id: Mapped[int] = mapped_column(ForeignKey("part_numbers.id"), index=True)
    type: Mapped[str] = mapped_column(String)

    part_number = relationship(
        "PartNumbers",
        foreign_keys=[part_number_id],
        back_populates="cross_refs_from"
    )

    cross_part_number = relationship(
        "PartNumbers",
        foreign_keys=[cross_part_number_id],
        back_populates="cross_refs_to"
    )


    __table_args__ = (
        UniqueConstraint("part_number_id", "cross_part_number_id"),
    )

    def __repr__(self):
        return f"<CrossReference id={self.id}>"


class PartFitment(Base):
    __tablename__ = "part_fitments"

    part_id: Mapped[int] = mapped_column(ForeignKey("parts.id"), index=True)
    car_modification_id: Mapped[int] = mapped_column(
        ForeignKey("car_modifications.id"),
        index=True
    )

    part = relationship("Part", back_populates="part_fitments")
    car_modification = relationship("CarModification", back_populates="part_fitments")


    __table_args__ = (
        UniqueConstraint("part_id", "car_modification_id"),
    )

    def __repr__(self):
        return  f"<PartFitment(id={self.id})>"
