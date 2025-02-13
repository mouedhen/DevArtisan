"""
Custom exception handlers for the FastAPI application.
"""

import logging
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = logging.getLogger(__name__)

async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """
    Handle HTTP exceptions and log the error.
    """
    logger.error(f"HTTP error occurred: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"HTTP error: {exc.detail}"}
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Handle validation exceptions and log the error.
    """
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=400,
        content={"message": "Validation error", "errors": exc.errors()}
    )