from app.orm_models.user import User
from app.pydantic_models.user import UserIn_Pydantic, User_Pydantic, Status
from typing import List
from fastapi import HTTPException, APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()


@router.get("/", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(User.all())


@router.post("/", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await User.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@router.get(
    "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def get_user(user_id: int):
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


@router.get(
    "/user/name/{user_name}"
)
# , response_model=any, responses={404: {"model": HTTPNotFoundError}}
async def get_user_name(user_name: str):
    queryset = (
        User.filter(name__icontains=user_name)
        .prefetch_related("phone")
    )
    result = await User_Pydantic.from_queryset(queryset)
    return result


@router.put(
    "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_user(user_id: int, user: UserIn_Pydantic):
    await User.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


@router.delete("/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")
