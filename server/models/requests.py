from datetime import datetime
from pydantic import BaseModel
from decimal import Decimal

class Requests(BaseModel):
    current_amount: Decimal
    wanted_amount: Decimal
    current_country: str
    current_city: str
    wanted_city: str
    current_bank: str
    wanted_bank: str
    current_purpose: str
    wanted_purpose: str
    wanted_country: str
    current_currency: str
    wanted_currency: str
    current_type: str
    wanted_type: str
    created_on: datetime

    class Config:
        orm_mode = True
