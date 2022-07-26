from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Messages(BaseModel):
    id: int
    deal_id: str
    author: str
    content: str
    type: str
    created_on: Optional[datetime]
    attached: Optional[bytes]

    class Config:
        orm_mode = True

