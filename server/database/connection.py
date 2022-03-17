from settings import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


engine = create_async_engine(
    settings.database_url
)

Session = sessionmaker(
    engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

async def getSession() -> Session:
    session = Session()
    try:
        yield session
    finally:
       await session.close()
