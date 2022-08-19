from database import tables
from database.connection import Session, getSession
from fastapi import Depends
from sqlalchemy import select
from database.tables import Requests, OpenDeals


class RequestService:
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    async def create(self, requestData: Requests):
        request = tables.Requests(**requestData.dict())
        self.session.add(request)
        await self.session.commit()


class RequestsService:
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    async def getList(self):
        result = await self.session.execute(select(Requests))
        return result.scalars().all()
    
    async def deleteRequest(self, id: Requests):
        result = await self.session.get(Requests, id)
        await self.session.delete(result)
        await self.session.commit()


class OpenDealsService:
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    async def create(self, dealData: OpenDeals):
        request = tables.OpenDeals(**dealData.dict())
        self.session.add(request)
        await self.session.commit()

    async def getList(self):
        result = await self.session.execute(select(OpenDeals))
        return result.scalars().all()

    async def deleteDeal(self, deal_id: OpenDeals):
        result = await self.session.get(OpenDeals, deal_id)
        await self.session.delete(result)
        await self.session.commit()




