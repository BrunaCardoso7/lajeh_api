from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from lajeh_api.settings import Settings

# engine=create_async_engine(Settings().DATABASE_URL, echo=True)
engine=create_async_engine("postgresql+asyncpg://lajeh_0_1_user:VeLw1y6KniThyeRZrhW005gSq6C4H46i@dpg-cu2t6qlumphs73b0nha0-a.oregon-postgres.render.com/lajeh_0_1", echo=True)


AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
) 

Base = declarative_base()

async def get_db():    
    async with AsyncSessionLocal() as session:
        yield session


def check_connection(engine):
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))