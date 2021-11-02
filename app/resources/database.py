from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise


def get_db_uri(user, password, host, db):
    # In case you want to use postgres as database
    return f'postgres://{user}:{password}@{host}:5432/{db}'


def setup_database(app: FastAPI):
    register_tortoise(
        app,
        db_url=get_db_uri("postgres", "postgres",
                          "localhost", "fastapitortoise"),
        modules={"models": ['app.orm_models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )


# We init the models here in order to define the models and get access to FK on queries.
Tortoise.init_models(['app.orm_models'], 'models')  # <- added
