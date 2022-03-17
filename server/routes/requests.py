from fastapi import APIRouter, Depends, HTTPException
from models.requests import Requests
from models.data import ErrorOutput
from services.requests import RequestService

request_router = APIRouter(
    prefix='/request'
)

@request_router.post('/create', response_model=Requests, responses={400: {'model': ErrorOutput}})
async def createRequest(requestData: Requests, service: RequestService = Depends()):
    try:
        return await service.create(requestData)
    except Exception as error:
        raise HTTPException(400, detail=str(error))
