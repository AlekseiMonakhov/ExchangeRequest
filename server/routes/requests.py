from fastapi import APIRouter, Depends
from typing import List
from database.connection import Session, getSession
from database import tables
from models.data import Countries, Currensies, PaymentType

router = APIRouter(
    prefix='/requests'
)

@router.post('/', response_model=List[Requests])
def getCountries(session: Session = Depends(getSession)):
    countries = (
        session
        .query(tables.Countries)
        .all()
    )
    return countries
