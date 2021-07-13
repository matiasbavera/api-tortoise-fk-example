from orm_models.user import Users
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True)


print(User_Pydantic.schema_json(indent=4))
