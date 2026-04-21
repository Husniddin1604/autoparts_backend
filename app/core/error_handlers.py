import traceback

from core.config import settings
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from schemas.error import ErrorResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from .exceptions import AppException


# Error handlers for the FastAPI application
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            status_code=exc.status_code, error=exc.error, detail=exc.detail
        ).model_dump(),
    )


# Validation error handler for request validation errors
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            status_code=422, error=str(exc.errors()), detail="ValidationError"
        ).model_dump(),
    )


# HTTP exception handler for Starlette HTTP exceptions
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            status_code=exc.status_code, error=exc.detail, detail="HTTPError"
        ).model_dump(),
    )


# General exception handler for unhandled exceptions
async def unhandled_exception_handler(request: Request, exc: Exception):
    traceback.print_exc()

    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            status_code=500,
            error="Unexpected error occurred. Please try again later.",
            detail="InternalServerError",
        ).model_dump(),
    )
