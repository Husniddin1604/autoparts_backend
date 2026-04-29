from typing import Annotated

from dependencies.uow import UowDependency
from fastapi import Depends

from services.ports import (
    ProductServiceABC,
    StockServiceABC,
    ProductAttributeValuesServiceABC,
)
from services.products import (
    ProductService,
    StockService,
    ProductAttributeValuesService,
)


def get_product_service(uow: UowDependency) -> ProductServiceABC:
    return ProductService(uow)


ProductServiceDep = Annotated[ProductServiceABC, Depends(get_product_service)]


def get_stock_service(uow: UowDependency) -> StockServiceABC:
    return StockService(uow)


StockServiceDep = Annotated[StockServiceABC, Depends(get_stock_service)]


def get_product_attribute_values_service(uow: UowDependency) -> ProductAttributeValuesServiceABC:
    return ProductAttributeValuesService(uow)


ProductAttributeValuesServiceDep = Annotated[ProductAttributeValuesServiceABC, Depends(get_product_attribute_values_service)]
