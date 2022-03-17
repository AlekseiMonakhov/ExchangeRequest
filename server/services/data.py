from sqlalchemy.future import select
from database.connection import Session, getSession
from fastapi import Depends
from database.tables import Countries, Currencies, PaymentType

class ContriesService():
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    async def getList(self):
        result = await self.session.execute(select(Countries))
        return result.scalars().all()

class CurrenciesService():
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    async def getList(self):
        result = await self.session.execute(select(Currencies))
        return result.scalars().all()

class PaymentTypeService():
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    async def getList(self):
        result = await self.session.execute(select(PaymentType))
        return result.scalars().all()

