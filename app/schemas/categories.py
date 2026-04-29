from pydantic import BaseModel, Field


class CategoryCreateRequest(BaseModel):
    parent_id: int | None = None
    name_uz: str = Field(..., min_length=1, max_length=255)
    name_ru: str = Field(..., min_length=1, max_length=255)
    name_en: str = Field(..., min_length=1, max_length=255)
    slug: str = Field(..., min_length=1, max_length=255)
    key: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., max_length=2000)
    sort_order: int = 0
    is_active: bool = True


class CategoryResponse(BaseModel):
    id: int
    parent_id: int | None
    name_uz: str
    name_ru: str
    name_en: str
    slug: str
    key: str
    description: str
    sort_order: int
    is_active: bool

    class Config:
        from_attributes = True


class AttributeCreateRequest(BaseModel):
    name_uz: str = Field(..., min_length=1, max_length=255)
    name_ru: str = Field(..., min_length=1, max_length=255)
    name_en: str = Field(..., min_length=1, max_length=255)
    unit: str = Field(..., max_length=50)
    data_type: str = Field(..., min_length=1, max_length=50)


class AttributeResponse(BaseModel):
    id: int
    name_uz: str
    name_ru: str
    name_en: str
    unit: str
    data_type: str

    class Config:
        from_attributes = True


class CategoryAttributeCreateRequest(BaseModel):
    category_id: int
    attribute_id: int
    is_filterable: bool = False
    is_required: bool = False


class CategoryAttributeResponse(BaseModel):
    id: int
    category_id: int
    attribute_id: int
    is_filterable: bool
    is_required: bool

    class Config:
        from_attributes = True


class PartCategoryLinksCreateRequest(BaseModel):
    part_id: int
    category_id: int
    is_primary: bool = False


class PartCategoryLinksResponse(BaseModel):
    id: int
    part_id: int
    category_id: int
    is_primary: bool

    class Config:
        from_attributes = True
