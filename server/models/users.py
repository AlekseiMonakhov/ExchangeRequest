import uuid
from typing import Optional
from pydantic import BaseModel, EmailStr, UUID4, Field


# class Users(BaseModel):
#     id: UUID4 = Field(default_factory=uuid.uuid4)
#     email: EmailStr = Field(default=None)
#     is_active: bool = True
#     is_superuser: bool = False
#     is_verified: bool = False
#     name: str
#     rank: Optional[str] = Field(default="5.0")
#     hashed_password: str
#
#     class Config:
#         orm_mode = True


class UserSchema(BaseModel):
    name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "name": "Alex",
                "email": "lexmonakhov@gmail.com",
                "password": "12345"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "email": "lexmonakhov@gmail.com",
                "password": "12345"
            }
        }

