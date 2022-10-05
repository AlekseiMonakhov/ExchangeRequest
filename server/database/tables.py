import uuid
from sqlalchemy import Integer, String, Column, DateTime, Numeric, Boolean, ForeignKey, Enum, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database.connection import engine
from sqlalchemy.orm import relationship
from sqlalchemy.util import asyncio

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True)
    email = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=72), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    rank = Column(Integer, nullable=True, default=0)


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
    created_on = Column(DateTime(), default=datetime.utcnow)
    profit = Column(String(255))
    maker_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), index=True)
    maker_rank = Column(Integer, nullable=False)
    maker_username = Column(String(255), nullable=False)

    user = relationship('User', backref='requests')


class OpenDeals(Base):
    __tablename__ = 'open_deals'
    deal_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer, nullable=False)
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
    created_on = Column(DateTime(), default=datetime.utcnow)
    status = Column(String(255), nullable=True, default="Инициирована")
    maker_id = Column(UUID(as_uuid=True), nullable=True)
    taker_id = Column(UUID(as_uuid=True), nullable=True)
    maker_username = Column(String(255), nullable=False)
    taker_username = Column(String(255), nullable=False)
    maker_rank = Column(Integer, nullable=True)
    taker_rank = Column(Integer, nullable=True)
    profit = Column(String(255), nullable=True)


class Messages(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True,  autoincrement=True)
    deal_id = Column(Integer, nullable=False)
    author = Column(String(255), nullable=False)
    content = Column(String(1020), nullable=True)
    type = Column(String(255), nullable=False)
    created_on = Column(DateTime(), default=datetime.utcnow)
    attached = Column(LargeBinary(), nullable=True)

async def async_create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def async_drop():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# asyncio.run(async_create())
