from datetime import date
from pydantic import BaseModel, Field


class ManufacturerCreateRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    image: str | None = Field(None, max_length=500)


class ManufacturerResponse(BaseModel):
    id: int
    name: str
    image: str | None

    class Config:
        from_attributes = True


class CarModelCreateRequest(BaseModel):
    manufacturer_id: int
    name: str = Field(..., min_length=1, max_length=255)
    generation: str = Field(..., min_length=1, max_length=100)
    start_year: date
    end_year: date | None = None


class CarModelResponse(BaseModel):
    id: int
    manufacturer_id: int
    name: str
    generation: str
    start_year: date
    end_year: date | None

    class Config:
        from_attributes = True


class CarModificationCreateRequest(BaseModel):
    model_id: int
    engine_code: str = Field(..., min_length=1, max_length=50)
    engine_volume: str = Field(..., min_length=1, max_length=50)
    fuel_type: str = Field(..., min_length=1, max_length=50)
    power_hp: str = Field(..., min_length=1, max_length=50)
    year_from: date
    year_to: date | None = None


class CarModificationResponse(BaseModel):
    id: int
    model_id: int
    engine_code: str
    engine_volume: str
    fuel_type: str
    power_hp: str
    year_from: date
    year_to: date | None

    class Config:
        from_attributes = True
