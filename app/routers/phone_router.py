from app.orm_models.phone import Phone
from app.pydantic_models.phone import PhoneIn_Pydantic, Phone_Pydantic
from app.pydantic_models.user import Status
from typing import List
from fastapi import HTTPException, APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()


@router.get("/", response_model=List[Phone_Pydantic])
async def get_phones():
    return await Phone_Pydantic.from_queryset(Phone.all())


@router.post("/", response_model=Phone_Pydantic)
async def create_phone(phone: PhoneIn_Pydantic):
    phone_obj = await Phone.create(**phone.dict(exclude_unset=True))
    return await Phone_Pydantic.from_tortoise_orm(phone_obj)


@router.get(
    "/phone/{phone_id}", response_model=Phone_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def get_phone(phone_id: int):
    return await Phone_Pydantic.from_queryset_single(Phone.get(id=phone_id))


@router.put(
    "/phone/{phone_id}", response_model=Phone_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_phone(phone_id: int, phone: PhoneIn_Pydantic):
    await Phone.filter(id=phone_id).update(**phone.dict(exclude_unset=True))
    return await Phone_Pydantic.from_queryset_single(Phone.get(id=phone_id))


@router.delete("/phone/{phone_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_phone(phone_id: int):
    deleted_count = await Phone.filter(id=phone_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"Phone {phone_id} not found")
    return Status(message=f"Deleted phone {phone_id}")
