from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.config import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT

POSTGRES_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(POSTGRES_URL, future=True, echo=False)

Session_local_async = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db() -> AsyncSession:
    async with Session_local_async() as session:
        yield session
