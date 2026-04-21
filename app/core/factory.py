from api.health import health_router
from api.v1 import main_router
from core.error_handlers import *
from core.exceptions import AppException
from core.lifespan import lifespan
from core.middleware import setup_middleware, setup_security_middleware
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


def create_app() -> FastAPI:
    app = FastAPI(
        title="Autoparts market",
        docs_url="/api/v1/swagger/",
        openapi_url="/api/v1/openapi.json",
        swagger_ui_parameters={"persistAuthorization": True},
        redoc_url=None,
        version="0.1.0",
        description="Autoparts market is a FastAPI application for autoparts market management and sales.",
        lifespan=lifespan,
    )

    # Register handlers
    app.add_exception_handler(AppException, app_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)

    setup_security_middleware(app)
    setup_middleware(app)

    app.include_router(health_router)
    app.include_router(main_router)

    return app