from fastapi import APIRouter
from .autoparts import router as autoparts_router
from .cars import router as cars_router
from .categories import router as categories_router
from .products import router as products_router

router = APIRouter(
    prefix="/shop",
)

all_routers = [
    autoparts_router,
    cars_router,
    categories_router,
    products_router
]

for r in all_routers:
    router.include_router(r)
