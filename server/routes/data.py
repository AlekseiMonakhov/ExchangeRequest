from fastapi import APIRouter, Depends
from typing import List
from database.connection import Session, getSession
from database import tables
from models.data import Countries, Currensies, PaymentType

router = APIRouter(
    prefix='/data'
)

@router.get('/countries', response_model=List[Countries])
def getCountries(session: Session = Depends(getSession)):
    countries = (
        session
        .query(tables.Countries)
        .all()
    )
    return countries

@router.get('/currencies', response_model=List[Currensies])
def getCurrencies(session: Session = Depends(getSession)):
    currencies = (
        session
        .query(tables.Currencies)
        .all()
    )
    return currencies

@router.get('/paymentType', response_model=List[PaymentType])
def getPaymentType(session: Session = Depends(getSession)):
    paymentType = (
        session
        .query(tables.PaymentType)
        .all()
    )
    return paymentType
