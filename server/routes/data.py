from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.data import Countries, Currensies, PaymentType, ErrorOutput
from services.data import ContriesService, CurrenciesService, PaymentTypeService

data_router = APIRouter(
    prefix='/data'
)

@data_router.get('/countries', response_model=List[Countries], responses={400: {'model': ErrorOutput}})
async def getCountries(service: ContriesService = Depends()):
    try:
        return await service.getList()
    except Exception as error:
        raise HTTPException(400, detail=str(error))\

@data_router.get('/currencies', response_model=List[Currensies], responses={400: {'model': ErrorOutput}})
async def getCurrencies(service: CurrenciesService = Depends()):
    try:
        return await service.getList()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@data_router.get('/paymentType', response_model=List[PaymentType], responses={400: {'model': ErrorOutput}})
async def getPaymentType(service: PaymentTypeService = Depends()):
    try:
        return await service.getList()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
