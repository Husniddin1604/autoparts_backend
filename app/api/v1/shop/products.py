from fastapi import APIRouter

from dependencies.products import (
    ProductServiceDep,
    StockServiceDep,
    ProductAttributeValuesServiceDep,
)
from schemas.products import (
    ProductResponse,
    StockResponse,
    ProductAttributeValuesResponse,
)


router = APIRouter(
    prefix="/products",
    tags=["shop-products"],
)


# Product endpoints (read-only)
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


# Stock endpoints (read-only)
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


# ProductAttributeValues endpoints (read-only)
@router.get("/{product_id}/attribute-values")
async def get_attribute_values_by_product_id(
    product_id: int,
    product_attribute_values_service: ProductAttributeValuesServiceDep,
) -> list[ProductAttributeValuesResponse]:
    return await product_attribute_values_service.get_attribute_values_by_product_id(product_id)
