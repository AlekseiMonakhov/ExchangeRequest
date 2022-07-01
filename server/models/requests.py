from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from decimal import Decimal
from pydantic.schema import Optional


class Requests(BaseModel):
    id: Optional[int]
    current_amount: Decimal
    wanted_amount: Decimal
    current_country: Optional[str]
    current_city: Optional[str]
    wanted_city: Optional[str]
    current_bank: Optional[str]
    wanted_bank: Optional[str]
    current_purpose: Optional[str]
    wanted_purpose: Optional[str]
    wanted_country: Optional[str]
    current_currency: str
    wanted_currency: str
    current_type: str
    wanted_type: str
    created_on: Optional[datetime]
    profit: str
    maker_id: UUID
    maker_rank: int
    maker_username: str

    class Config:
        orm_mode = True


class OpenDeals(BaseModel):
    deal_id: Optional[int]
    id: Optional[int]
    current_amount: Decimal
    wanted_amount: Decimal
    current_country: Optional[str]
    current_city: Optional[str]
    wanted_city: Optional[str]
    current_bank: Optional[str]
    wanted_bank: Optional[str]
    current_purpose: Optional[str]
    wanted_purpose: Optional[str]
    wanted_country: Optional[str]
    current_currency: str
    wanted_currency: str
    current_type: str
    wanted_type: str
    created_on: Optional[datetime]
    profit: str
    status: Optional[str]
    maker_id: Optional[UUID]
    taker_id: Optional[UUID]
    maker_rank: Optional[int]
    taker_rank: Optional[int]
    maker_username: str
    taker_username: str

    class Config:
        orm_mode = True
