from typing import List

from fastapi import APIRouter

from core.infra.builder.user_builder import UserBuilder
from core.infra.factory.user_service_factory import UserServiceFactory
from core.infra.schema.user import CreateUser, UpdateUser, User

user_router = APIRouter(
    tags=["User"],
    prefix="/user",
    responses={404: {"description": "Not found"}},
)
user_service = UserServiceFactory().create()


@user_router.get("/", response_model=List[User])
async def list_user():
    return user_service.user_repository.find_all()


@user_router.get("/{id}", response_model=User)
async def get_user(id: str):
    return user_service.user_repository.find(id=id)


@user_router.post("/", response_model=User)
async def create_user(user: CreateUser):
    user_builder = UserBuilder()
    created_user = user_service.create(
        user=user_builder.build(dict(user)),
    )
    return created_user


@user_router.put("/{id}", response_model=User)
async def update_power_data(id: str, power_data: UpdateUser):
    user_builder = UserBuilder()
    created_user = user_service.update(
        user=user_builder.build({"id": id, **dict(power_data)}),
    )
    return created_user


@user_router.delete("/{id}")
async def update_power_data(id: str):
    user_service.delete(id)
