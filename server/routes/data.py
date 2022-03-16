from fastapi import APIRouter, Depends
from typing import List
from models.data import Countries, Currensies, PaymentType
from services.data import ContriesService, CurrenciesService, PaymentTypeService

router = APIRouter(
    prefix='/data'
)

@router.get('/countries', response_model=List[Countries])
def getCountries(service: ContriesService = Depends()):
    return service.getList()

@router.get('/currencies', response_model=List[Currensies])
def getCurrencies(service: CurrenciesService = Depends()):
    return service.getList()

@router.get('/paymentType', response_model=List[PaymentType])
def getPaymentType(service: PaymentTypeService = Depends()):
    return service.getList()
