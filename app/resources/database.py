from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise


def get_db_uri(*, user, password, host, db):
    return f'postgres://{user}:{password}@{host}:5432/{db}'


def setup_database(app: FastAPI):

    register_tortoise(
        app,
        db_url="sqlite://:memory:",
        modules={"models": ['orm_models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )


Tortoise.init_models(
    ['orm_models'], 'models')  # <- added
