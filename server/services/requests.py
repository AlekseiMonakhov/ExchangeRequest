from typing import List
from database import tables
from database.connection import Session, getSession
from fastapi import Depends

from database.tables import Requests


class RequestService():
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    def create(self, requestData: Requests) -> tables.Requests:
        request = tables.Requests(**requestData.dict())
        self.session.add(request)
        self.session.commit()
        return request
