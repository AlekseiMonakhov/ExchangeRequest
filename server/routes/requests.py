from fastapi import APIRouter, Depends
from models.requests import Requests
from services.requests import RequestService

request_router = APIRouter(
    prefix='/requests'
)

@request_router.post('/', response_model=Requests)
def createRequest(
    requestData: Requests,
    service: RequestService = Depends()
):
    return service.create(requestData)
