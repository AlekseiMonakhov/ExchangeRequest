from pydantic import BaseModel


class Countries(BaseModel):
    id: int
    country_name: str

    class Config:
        orm_mode = True


class Currencies(BaseModel):
    id: int
    currency_name: str

    class Config:
        orm_mode = True


class PaymentType(BaseModel):
    id: int
    type: str

    class Config:
        orm_mode = True


class Cities(BaseModel):
    id: int
    city_name: str

    class Config:
        orm_mode = True


class Banks(BaseModel):
    id: int
    bank_name: str
    country: str

    class Config:
        orm_mode = True


class Purposes(BaseModel):
    id: int
    purpose: str

    class Config:
        orm_mode = True


class ErrorOutput(BaseModel):
    detail: str
