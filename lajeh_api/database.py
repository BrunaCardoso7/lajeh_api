from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from lajeh_api.settings import Settings
from typing import AsyncGenerator


# engine=create_async_engine(Settings().DATABASE_URL, echo=True)
engine=create_async_engine(
    "postgresql+asyncpg://lajeh_0_1_user:VeLw1y6KniThyeRZrhW005gSq6C4H46i@dpg-cu2t6qlumphs73b0nha0-a.oregon-postgres.render.com/lajeh_0_1", 
    echo=True
)


AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
) 

Base = declarative_base()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

async def check_connection():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))  # Executando um simples SELECT para verificar
        print("Conexão bem-sucedida com o banco de dados!")