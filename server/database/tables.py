import asyncio
from sqlalchemy import Integer, String, Column, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from connection import engine

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

class Requests(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    current_amount = Column(Numeric(10, 2), nullable=False)
    current_country = Column(String(255), nullable=False)
    current_currency = Column(String(255), nullable=False)
    current_type = Column(String(255), nullable=False)
    wanted_amount = Column(Numeric(10, 2), nullable=False)
    wanted_country = Column(String(255), nullable=False)
    wanted_currency = Column(String(255), nullable=False)
    wanted_type = Column(String(255), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)


async def async_create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def async_drop():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

#asyncio.run(async_create())
