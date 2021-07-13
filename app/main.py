# pylint: disable=E0611,E0401
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from resources.database import setup_database
from orm_models.user import Users
from pydantic_models.user import UserIn_Pydantic, User_Pydantic
from routers.user_router import router as UserRouter

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI(title="Tortoise ORM FastAPI example")


class Status(BaseModel):
    message: str


app.include_router(UserRouter, tags=["User"], prefix="/user")


@app.on_event("startup")
async def startup_event():
    setup_database(app)
