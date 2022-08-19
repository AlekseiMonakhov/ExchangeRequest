from typing import List
from fastapi import APIRouter, Depends, HTTPException
from models.requests import Requests, OpenDeals
from models.data import ErrorOutput
from services.requests import RequestService, RequestsService, OpenDealsService

request_router = APIRouter(
    prefix='/request'
)


@request_router.post('/create', response_model=Requests, responses={400: {'model': ErrorOutput}})
async def createRequest(requestData: Requests, service: RequestService = Depends()):
    try:
        return await service.create(requestData)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@request_router.post('/open-deal', response_model=OpenDeals, responses={400: {'model': ErrorOutput}})
async def openDeal(dealData: OpenDeals, service: OpenDealsService = Depends()):
    try:
        return await service.create(dealData)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@request_router.delete('/delete-deal/{deal_id}')
async def openDeal(deal_id: int, service: OpenDealsService = Depends()):
    try:
        return await service.deleteDeal(deal_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@request_router.delete('/delete-request/{request_id}')
async def deleteRequest(request_id: int, service: RequestsService = Depends()):
    try:
        return await service.deleteRequest(request_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@request_router.get('/getlist', response_model=List[Requests], responses={400: {'model': ErrorOutput}})
async def getRequests(service: RequestsService = Depends()):
    try:
        return await service.getList()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@request_router.get('/getOpenDeals', response_model=List[OpenDeals], responses={400: {'model': ErrorOutput}})
async def getOpenDeals(service: OpenDealsService = Depends()):
    try:
        return await service.getList()
    except Exception as error:
        raise HTTPException(400, detail=str(error))



