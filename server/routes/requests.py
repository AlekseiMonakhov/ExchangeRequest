from fastapi import APIRouter, Depends
from typing import List
from models.requests import Requests
from services.requests import RequestService

router = APIRouter(
    prefix='/requests'
)

@router.post('/', response_model=Requests)
def createRequest(
    requestData: Requests,
    service: RequestService = Depends()
):
    return service.create(requestData)
