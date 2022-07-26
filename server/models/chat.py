from datetime import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, UUID4, Field
from sqlalchemy import LargeBinary


class BaseUser(BaseModel):
    id: int
    deal_id: str
    author: str
    content: str
    type: str
    created_on: Optional[datetime]
    attached = Optional[LargeBinary]

    class Config:
        orm_mode = True

