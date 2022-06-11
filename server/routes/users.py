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



