from datetime import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, UUID4, Field
from sqlalchemy import LargeBinary


class BaseUser(BaseModel):
    id: Optional[int]
    deal_id: int
    author: str
    content: Optional[str]
    type: str
    created_on: Optional[datetime]
    attached = Optional[bytes]

    class Config:
        orm_mode = True
