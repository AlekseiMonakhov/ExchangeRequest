import asyncio
from sqlalchemy import Integer, String, Column, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database.connection import engine

Base = declarative_base()


class Countries(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    country_name = Column(String(255), nullable=False)


class Currencies(Base):
    __tablename__ = 'currencies'
    id = Column(Integer, primary_key=True)
    currency_name = Column(String(255), nullable=False)


class PaymentType(Base):
    __tablename__ = 'payment_type'
    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)


class Cities(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    city_name = Column(String(255), nullable=False)


class Banks(Base):
    __tablename__ = 'banks'
    id = Column(Integer, primary_key=True)
    country = Column(String(255), nullable=True)
    bank_name = Column(String(255), nullable=False)


class Purposes(Base):
    __tablename__ = 'purposes'
    id = Column(Integer, primary_key=True)
    purpose = Column(String(255), nullable=False)


class Requests(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    current_amount = Column(Numeric(10, 2), nullable=False)
    wanted_amount = Column(Numeric(10, 2), nullable=False)
    current_country = Column(String(255), nullable=True)
    wanted_country = Column(String(255), nullable=True)
    current_city = Column(String(255), nullable=True)
    wanted_city = Column(String(255), nullable=True)
    current_bank = Column(String(255), nullable=True)
    wanted_bank = Column(String(255), nullable=True)
    current_purpose = Column(String(255), nullable=True)
    wanted_purpose = Column(String(255), nullable=True)
    current_currency = Column(String(255), nullable=False)
    wanted_currency = Column(String(255), nullable=False)
    current_type = Column(String(255), nullable=False)
    wanted_type = Column(String(255), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    profit = Column(String(255))


class OpenDeals(Base):
    __tablename__ = 'open_deals'
    id = Column(Integer, primary_key=True, autoincrement=True)
    current_amount = Column(Numeric(10, 2), nullable=False)
    wanted_amount = Column(Numeric(10, 2), nullable=False)
    current_country = Column(String(255), nullable=True)
    wanted_country = Column(String(255), nullable=True)
    current_city = Column(String(255), nullable=True)
    wanted_city = Column(String(255), nullable=True)
    current_bank = Column(String(255), nullable=True)
    wanted_bank = Column(String(255), nullable=True)
    current_purpose = Column(String(255), nullable=True)
    wanted_purpose = Column(String(255), nullable=True)
    current_currency = Column(String(255), nullable=False)
    wanted_currency = Column(String(255), nullable=False)
    current_type = Column(String(255), nullable=False)
    wanted_type = Column(String(255), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    status = Column(String(255), nullable=True, default="Инициирована")
    maker_id = Column(String(255), nullable=True, default="12345678")
    taker_id = Column(String(255), nullable=True, default="23456789")
    maker_rank = Column(String(255), nullable=True, default="5.0")
    taker_rank = Column(String(255), nullable=True, default="5.0")
    profit = Column(String(255), nullable=True, default="1%")


async def async_create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def async_drop():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# asyncio.run(async_create())
