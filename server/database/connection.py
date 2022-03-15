from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
import os

load_dotenv()
env_path = Path('..')/'.env'
load_dotenv(dotenv_path=env_path)


DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession)

engine.connect()
print(engine)
