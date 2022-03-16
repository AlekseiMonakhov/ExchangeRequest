from typing import List
from database import tables
from database.connection import Session, getSession
from fastapi import Depends

class ContriesService():
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    def getList(self) -> List[tables.Countries]:
        countries = (
            self.session
            .query(tables.Countries)
            .all()
        )
        return countries

class CurrenciesService():
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    def getList(self) -> List[tables.Currencies]:
        currencies = (
            self.session
            .query(tables.Currencies)
            .all()
        )
        return currencies

class PaymentTypeService():
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    def getList(self) -> List[tables.PaymentType]:
        paymentType = (
            self.session
            .query(tables.PaymentType)
            .all()
        )
        return paymentType


