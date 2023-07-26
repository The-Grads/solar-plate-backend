from fastapi import FastAPI

from core.infra.controller import core_router

from .utils.exception_handler import exception_handler

app = FastAPI()

app.include_router(core_router)
app.add_exception_handler(Exception, exception_handler)
