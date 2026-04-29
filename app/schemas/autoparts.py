from pydantic import BaseModel, Field


class BrandCreateRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    country: str | None = Field(None, max_length=255)
    is_oem: bool = False


class BrandResponse(BaseModel):
    id: int
    name: str
    country: str | None
    is_oem: bool

    class Config:
        from_attributes = True


class PartCreateRequest(BaseModel):
    name_uz: str = Field(..., min_length=1, max_length=500)
    name_ru: str = Field(..., min_length=1, max_length=500)
    name_en: str = Field(..., min_length=1, max_length=500)
    slug: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., max_length=2000)


class PartResponse(BaseModel):
    id: int
    name_uz: str
    name_ru: str
    name_en: str
    slug: str
    description: str

    class Config:
        from_attributes = True


class PartNumbersCreateRequest(BaseModel):
    part_id: int
    brand_id: int
    number: str = Field(..., min_length=1, max_length=100)
    is_oem: bool = False
    replaced_by_id: int | None = None


class PartNumbersResponse(BaseModel):
    id: int
    part_id: int
    brand_id: int
    number: str
    is_oem: bool
    replaced_by_id: int | None

    class Config:
        from_attributes = True


class CrossReferenceCreateRequest(BaseModel):
    part_number_id: int
    cross_part_number_id: int
    type: str = Field(..., min_length=1, max_length=50)


class CrossReferenceResponse(BaseModel):
    id: int
    part_number_id: int
    cross_part_number_id: int
    type: str

    class Config:
        from_attributes = True


class PartFitmentCreateRequest(BaseModel):
    part_id: int
    car_modification_id: int


class PartFitmentResponse(BaseModel):
    id: int
    part_id: int
    car_modification_id: int

    class Config:
        from_attributes = True
