from fastapi import APIRouter
from .auth import router as auth_router
from .users import router as users_router
from .autoparts import router as autoparts_router
from .cars import router as cars_router
from .categories import router as categories_router
from .products import router as products_router

main_router = APIRouter()

all_routers = [
    auth_router,
    users_router,
    autoparts_router,
    cars_router,
    categories_router,
    products_router
]
for router in all_routers:
    main_router.include_router(router, prefix="/api/v1")