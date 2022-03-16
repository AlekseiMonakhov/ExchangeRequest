from pydantic import BaseModel

class Countries(BaseModel):
    id: int
    country_name: str

    class Config:
        orm_mode = True

class Currensies(BaseModel):
    id: int
    currency_name: str

    class Config:
        orm_mode = True

class PaymentType(BaseModel):
    id: int
    type: str

    class Config:
        orm_mode = True



