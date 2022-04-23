from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.data import Countries, Currensies, PaymentType, ErrorOutput, Banks, Cities, Purposes
from services.data import ContriesService, CurrenciesService, PaymentTypeService, CitiesService, BanksService, PurposesService

data_router = APIRouter(
    prefix='/data'
)

# @data_router.get('/countries', response_model=List[Countries, Currensies, PaymentType, Cities, Banks, Purposes], responses={400: {'model': ErrorOutput}})
# async def getCountries(service: DataService = Depends()):
#     try:
#         return await service.getList()
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))


@data_router.get('/countries', response_model=List[Countries], responses={400: {'model': ErrorOutput}})
async def getCountries(service: ContriesService = Depends()):
    try:
        return await service.getList()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

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

@data_router.get('/cities', response_model=List[Cities], responses={400: {'model': ErrorOutput}})
async def getCities(service: CitiesService = Depends()):
    try:
        return await service.getList()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@data_router.get('/banks', response_model=List[Banks], responses={400: {'model': ErrorOutput}})
async def getBanks(service: BanksService = Depends()):
    try:
        return await service.getList()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@data_router.get('/purposes', response_model=List[Purposes], responses={400: {'model': ErrorOutput}})
async def getPurposes(service: PurposesService = Depends()):
    try:
        return await service.getList()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
