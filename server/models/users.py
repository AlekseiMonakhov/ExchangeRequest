import uuid
from typing import Optional
from pydantic import BaseModel, EmailStr, UUID4, Field


class User(BaseModel):
    # id: UUID4 = Field(default_factory=uuid.uuid4)
    # email: EmailStr = Field(default=None)
    # is_active: bool = True
    # is_superuser: bool = False
    # is_verified: bool = False
    # name: str
    # rank: Optional[str] = Field(default="5.0")
    # hashed_password: str

    class Config:
        orm_mode = True



class BaseUser(BaseModel):
    email: str
    username: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

