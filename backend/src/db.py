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


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    score = Column(Float, nullable=True)
    description = Column(String, nullable=False)
    genre = Column(String, nullable=False)

class Actor(Base):
    __tablename__ = "actors"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)

class Movie_Actor(Base):
    __tablename__ = "movie_actor"

    movie_id = Column(Uuid(as_uuid=True), ForeignKey("movies.id"), primary_key=True)
    actor_id = Column(Uuid(as_uuid=True), ForeignKey("actors.id"), primary_key=True)

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session