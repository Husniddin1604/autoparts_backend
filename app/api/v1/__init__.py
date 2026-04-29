from fastapi import APIRouter
from .auth import router as auth_router
from .users import router as users_router
from .shop import router as shop_router
from .admin import router as admin_router

main_router = APIRouter()

all_routers = [
    auth_router,
    users_router,
    shop_router,
    admin_router
]
for router in all_routers:
    main_router.include_router(router, prefix="/api/v1")