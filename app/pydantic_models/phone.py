from pydantic import BaseModel
from app.orm_models.phone import Phone
from tortoise.contrib.pydantic import pydantic_model_creator


Phone_Pydantic = pydantic_model_creator(Phone, name="Phone")
PhoneIn_Pydantic = pydantic_model_creator(
    Phone, name="PhoneIn", exclude_readonly=True)
