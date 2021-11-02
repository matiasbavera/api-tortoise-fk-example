from pydantic import BaseModel
from app.orm_models.user import User
from tortoise.contrib.pydantic import pydantic_model_creator


User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(
    User, name="UserIn", exclude_readonly=True)


print(User_Pydantic.schema_json(indent=4))


class Status(BaseModel):
    message: str
