from fastapi import APIRouter, status

from dependencies.products import (
    ProductServiceDep,
    StockServiceDep,
    ProductAttributeValuesServiceDep,
)
from schemas.products import (
    ProductCreateRequest,
    ProductResponse,
    StockCreateRequest,
    StockResponse,
    StockUpdateRequest,
    StockReservedUpdateRequest,
    ProductAttributeValuesCreateRequest,
    ProductAttributeValuesResponse,
)


router = APIRouter(
    prefix="/products",
    tags=["admin-products"],
)


# Product endpoints (write operations)
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(
    product_info: ProductCreateRequest,
    product_service: ProductServiceDep,
) -> ProductResponse:
    return await product_service.create_product(product_info)


@router.get("/barcode/{barcode}")
async def get_product_by_barcode(
    barcode: str,
    product_service: ProductServiceDep,
) -> ProductResponse:
    return await product_service.get_product_by_barcode(barcode)


@router.get("/part-numbers/{part_number_id}")
async def get_products_by_part_number_id(
    part_number_id: int,
    product_service: ProductServiceDep,
) -> list[ProductResponse]:
    return await product_service.get_products_by_part_number_id(part_number_id)


@router.get("/{product_id}")
async def get_product(
    product_id: int,
    product_service: ProductServiceDep,
) -> ProductResponse:
    return await product_service.get_product_by_id(product_id)


# Stock endpoints (write operations)
@router.post("/stocks", status_code=status.HTTP_201_CREATED)
async def create_stock(
    stock_info: StockCreateRequest,
    stock_service: StockServiceDep,
) -> StockResponse:
    return await stock_service.create_stock(stock_info)


@router.get("/stocks/{stock_id}")
async def get_stock(
    stock_id: int,
    stock_service: StockServiceDep,
) -> StockResponse:
    return await stock_service.get_stock_by_id(stock_id)


@router.get("/{product_id}/stocks")
async def get_stocks_by_product_id(
    product_id: int,
    stock_service: StockServiceDep,
) -> list[StockResponse]:
    return await stock_service.get_stocks_by_product_id(product_id)


@router.put("/stocks/{stock_id}/quantity")
async def update_stock_quantity(
    stock_id: int,
    quantity_update: StockUpdateRequest,
    stock_service: StockServiceDep,
) -> StockResponse:
    return await stock_service.update_stock_quantity(stock_id, quantity_update.quantity)


@router.put("/stocks/{stock_id}/reserved-quantity")
async def update_stock_reserved_quantity(
    stock_id: int,
    reserved_quantity_update: StockReservedUpdateRequest,
    stock_service: StockServiceDep,
) -> StockResponse:
    return await stock_service.update_stock_reserved_quantity(stock_id, reserved_quantity_update.reserved_quantity)


# ProductAttributeValues endpoints (write operations)
@router.post("/attribute-values", status_code=status.HTTP_201_CREATED)
async def create_product_attribute_value(
    attribute_value_info: ProductAttributeValuesCreateRequest,
    product_attribute_values_service: ProductAttributeValuesServiceDep,
) -> ProductAttributeValuesResponse:
    return await product_attribute_values_service.create_product_attribute_value(attribute_value_info)


@router.get("/{product_id}/attribute-values")
async def get_attribute_values_by_product_id(
    product_id: int,
    product_attribute_values_service: ProductAttributeValuesServiceDep,
) -> list[ProductAttributeValuesResponse]:
    return await product_attribute_values_service.get_attribute_values_by_product_id(product_id)
