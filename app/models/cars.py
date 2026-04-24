from datetime import date

from models.base import Base
from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Manufacturer(Base):
    __tablename__ = "manufacturers"

    name: Mapped[str] = mapped_column(String)
    image: Mapped[str | None] = mapped_column(String, nullable=True)

    car_models = relationship("CarModel", back_populates="manufacturer")

    def __repr__(self):
        return self.name


class CarModel(Base):
    __tablename__ = "car_models"

    manufacturer_id: Mapped[int] = mapped_column(ForeignKey("manufacturers.id"), index=True)
    name: Mapped[str] = mapped_column(String)
    generation: Mapped[str] = mapped_column(String)
    start_year: Mapped[date] = mapped_column(Date)
    end_year: Mapped[date | None] = mapped_column(Date, nullable=True)

    manufacturer: Mapped[Manufacturer] = relationship("Manufacturer", back_populates="car_models")
    car_modifications = relationship("CarModification", back_populates="model")

    def __repr__(self):
        return f"{self.name} {self.generation} {self.start_year} - {self.end_year}"


class CarModification(Base):
    __tablename__ = "car_modifications"

    model_id: Mapped[int] = mapped_column(ForeignKey("car_models.id"), index=True)
    engine_code: Mapped[str] = mapped_column(String)
    engine_volume: Mapped[str] = mapped_column(String)
    fuel_type: Mapped[str] = mapped_column(String)
    power_hp: Mapped[str] = mapped_column(String)
    year_from: Mapped[date] = mapped_column(Date)
    year_to: Mapped[date | None] = mapped_column(Date, nullable=True)

    model: Mapped[CarModel] = relationship("CarModel", back_populates="car_modifications")
    part_fitments = relationship("PartFitment", back_populates="car_modification")

    def __repr__(self):
        return f"{self.engine_code} {self.engine_volume} {self.fuel_type} {self.power_hp} {self.year_from} - {self.year_to}"

