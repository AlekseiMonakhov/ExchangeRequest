import uuid
from typing import Optional
from pydantic import BaseModel, UUID4, Field


class BaseUser(BaseModel):
    email: str
    username: str

    class Config:
        orm_mode = True


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: UUID4
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    rank: int


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

    class Config:
        orm_mode = True
