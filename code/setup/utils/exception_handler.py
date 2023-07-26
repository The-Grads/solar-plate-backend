import sys
import traceback

from fastapi import Request
from fastapi.responses import JSONResponse

from .logger import logger


async def exception_handler(request: Request, exc: Exception) -> JSONResponse:
    host = getattr(getattr(request, "client", None), "host", None)
    port = getattr(getattr(request, "client", None), "port", None)
    url = (
        f"{request.url.path}?{request.query_params}"
        if request.query_params
        else request.url.path
    )

    exception_type, exception_value, exception_traceback = sys.exc_info()
    exception_name = getattr(exception_type, "__name__", None)

    logger.error(traceback.format_exc())
    logger.error(
        f'{host}:{port} - "{request.method} {url}" 500 Internal Server Error <{exception_name}: {exception_value}>'
    )

    return JSONResponse(
        content={"error": exception_name, "message": str(exception_value)},
        status_code=500,
    )
