from typing import List
from fastapi import APIRouter, Depends, HTTPException, APIRouter, Depends, status
from models.users import User, Token, UserCreate
from models.data import ErrorOutput
from fastapi import (
    APIRouter,
    Depends,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm
from services.users import (
    AuthService,
    get_current_user,
)

user_router = APIRouter(
    prefix='/user'
)


# @user_router.post('signup', response_model=UserSchema, responses={400: {'model': ErrorOutput}})
# async def userSignup(user: UserSchema, service: UserService = Depends()):
#     try:
#         return await service.create(user)
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))
#
#
@user_router.post(
    '/sign-up/',
    response_model=Token,
    status_code=status.HTTP_201_CREATED,
)
async def sign_up(
    user_data: UserCreate,
    auth_service: AuthService = Depends(),
):
    return await auth_service.register_new_user(user_data)


@user_router.post(
    '/sign-in/',
    response_model=Token,
)
async def sign_in(
    auth_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(),
):
    return await auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )


@user_router.get(
    '/user/',
    response_model=User,
)
async def get_user(user: User = Depends(get_current_user)):
    return user
