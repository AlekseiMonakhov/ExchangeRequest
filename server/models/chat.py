from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Messages(BaseModel):
    id: Optional[int]
    deal_id: int
    author: str
    content: Optional[str]
    type: str
    created_on: Optional[datetime]
    attached: Optional[bytes]

    class Config:
        orm_mode = True
