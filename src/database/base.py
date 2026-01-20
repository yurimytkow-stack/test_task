from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import text
from fastapi import HTTPException, status

from config.config import settings

DATABASE_URL = settings.DATABASE_URL

async_engine = create_async_engine(
    DATABASE_URL,
    pool_timeout=300,
)

async_session = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()
