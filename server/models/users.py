import uuid
from typing import Optional
from pydantic import BaseModel, UUID4, Field


class BaseUser(BaseModel):
    email: str
    username: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: UUID4
    hashed_password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: Optional[str]
    token_type: str = 'bearer'

    class Config:
        orm_mode = True
