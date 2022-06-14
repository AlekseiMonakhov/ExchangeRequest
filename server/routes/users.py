from typing import List
from fastapi import APIRouter, Depends, HTTPException
from models.requests import Requests, OpenDeals, Users, UserShema
from models.data import ErrorOutput
from models.users import UserSchema
from services.requests import RequestService, RequestsService, OpenDealsService

user_router = APIRouter(
    prefix='/user'
)


@user_router.post('signup', response_model=UserSchema, responses={400: {'model': ErrorOutput}})
async def userSignup(user: UserSchema, service: UserService = Depends()):
    try:
        return await service.create(user)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

# @request_router.post('/create', response_model=Requests, responses={400: {'model': ErrorOutput}})
# async def createRequest(requestData: Requests, service: RequestService = Depends()):
#     try:
#         return await service.create(requestData)
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))
#
#
# @request_router.post('/open-deal', response_model=OpenDeals, responses={400: {'model': ErrorOutput}})
# async def openDeal(dealData: OpenDeals, service: OpenDealsService = Depends()):
#     try:
#         return await service.create(dealData)
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))
#
#
# @request_router.delete('/delete/{deal_id}')
# async def openDeal(deal_id: int, service: OpenDealsService = Depends()):
#     try:
#         return await service.deleteDeal(deal_id)
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))
#
#
# @request_router.get('/getlist', response_model=List[Requests], responses={400: {'model': ErrorOutput}})
# async def getRequests(service: RequestsService = Depends()):
#     try:
#         return await service.getList()
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))
#
#
# @request_router.get('/getOpenDeals', response_model=List[OpenDeals], responses={400: {'model': ErrorOutput}})
# async def getOpenDeals(service: OpenDealsService = Depends()):
#     try:
#         return await service.getList()
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))

#
# from fastapi import (
#     APIRouter,
#     Depends,
#     status,
# )
# from fastapi.security import OAuth2PasswordRequestForm
#
# from .. import models
# from ..services.auth import (
#     AuthService,
#     get_current_user,
# )
#
#
# router = APIRouter(
#     prefix='/auth',
#     tags=['auth'],
# )
#
#
# @router.post(
#     '/sign-up/',
#     response_model=models.Token,
#     status_code=status.HTTP_201_CREATED,
# )
# def sign_up(
#     user_data: models.UserCreate,
#     auth_service: AuthService = Depends(),
# ):
#     return auth_service.register_new_user(user_data)
#
#
# @router.post(
#     '/sign-in/',
#     response_model=models.Token,
# )
# def sign_in(
#     auth_data: OAuth2PasswordRequestForm = Depends(),
#     auth_service: AuthService = Depends(),
# ):
#     return auth_service.authenticate_user(
#         auth_data.username,
#         auth_data.password,
#     )
#
#
# @router.get(
#     '/user/',
#     response_model=models.User,
# )
# def get_user(user: models.User = Depends(get_current_user)):
#     return user
