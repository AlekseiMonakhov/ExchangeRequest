from pydantic import BaseModel
from decimal import Decimal

class Requests(BaseModel):
    current_amount: Decimal
    wanted_amount: Decimal
    current_country: str
    wanted_country: str
    current_currency: str
    wanted_currency: str
    current_type: str
    wanted_type: str

    class Config:
        orm_mode = True
