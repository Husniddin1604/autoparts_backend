from decimal import Decimal
from pydantic import BaseModel, Field


class ProductCreateRequest(BaseModel):
    part_number_id: int
    name: str = Field(..., min_length=1, max_length=500)
    selling_price: Decimal = Field(..., gt=0)
    barcode: str = Field(..., min_length=1, max_length=100)


class ProductResponse(BaseModel):
    id: int
    part_number_id: int
    name: str
    selling_price: Decimal
    barcode: str

    class Config:
        from_attributes = True


class StockCreateRequest(BaseModel):
    product_id: int
    quantity: int = Field(default=0, ge=0)
    reserved_quantity: int = Field(default=0, ge=0)
    purchase_price: Decimal = Field(..., gt=0)


class StockResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    reserved_quantity: int
    purchase_price: Decimal

    class Config:
        from_attributes = True


class StockUpdateRequest(BaseModel):
    quantity: int = Field(..., ge=0)


class StockReservedUpdateRequest(BaseModel):
    reserved_quantity: int = Field(..., ge=0)


class ProductAttributeValuesCreateRequest(BaseModel):
    product_id: int
    attribute_id: int
    value_text: str | None = Field(None, max_length=500)
    value_number: Decimal | None = None


class ProductAttributeValuesResponse(BaseModel):
    id: int
    product_id: int
    attribute_id: int
    value_text: str | None
    value_number: Decimal | None

    class Config:
        from_attributes = True
