from collections.abc import AsyncGenerator
import uuid
from sqlalchemy import Integer, Float
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
import datetime
from sqlalchemy import Uuid
DATABASE_URL = "sqlite+aiosqlite:///C:/Users/danie/Movies/backend/test.db"

class Base(DeclarativeBase):
    pass

class UserAccount(Base):
    __tablename__ = "users_account"

    user_id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)

    username = Column(String, nullable=False, unique=True)
    hashed_paasword = Column(String, nullable=False)

class Director(Base):
    __tablename__ = "director"

    director_id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)

    director_name = Column(String, nullable=False)
    director_surname = Column(String, nullable=False)
    director_birthdate = Column(Date)
    director_biography = Column(Text)

class Actor(Base):
    __tablename__ = "actor"

    actor_id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)

    actor_name = Column(String, nullable=False)
    actor_surname = Column(String, nullable=False)
    actor_birthdate = Column(Date)
    actor_biography = Column(Text)

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session