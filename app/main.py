# pylint: disable=E0611,E0401
from typing import List
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from app.resources.database import setup_database
from app.routers.user_router import router as UserRouter

app = FastAPI(title="Tortoise + FastAPI")


@app.on_event("startup")
async def startup_event():
    setup_database(app)


@app.exception_handler(HTTPException)
async def unicorn_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

app.include_router(UserRouter, tags=["User"], prefix="/user")
