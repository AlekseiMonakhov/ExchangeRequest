from typing import List

from sqlalchemy.future import select

from database import tables
from database.connection import Session, getSession
from fastapi import Depends

from database.tables import Requests


class RequestService():
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    async def create(self, requestData: Requests):
        request = tables.Requests(**requestData.dict())
        self.session.add(request)
        await self.session.commit()

