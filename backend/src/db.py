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

    movies_director = relationship("Movie", secondary="director_movie", back_populates="directors")

class Actor(Base):
    __tablename__ = "actor"

    actor_id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)

    actor_name = Column(String, nullable=False)
    actor_surname = Column(String, nullable=False)
    actor_birthdate = Column(Date)
    actor_biography = Column(Text)

    movies = relationship("Movie",secondary="movie_actor",back_populates="actors")

class Genre(Base):
    __tablename__ = "genres"

    genre_id = Column(Integer, primary_key=True, autoincrement=True)

    genre = Column(String, nullable=False, unique=True)

class Movie(Base):
    __tablename__ = "movie"

    movie_id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)

    movie_title = Column(String, nullable=False)
    movie_user_rating = Column(Float, nullable=True)
    movie_critic_rating = Column(Float, nullable=True)
    movie_duration_min = Column(Integer, nullable=True)
    movie_description = Column(Text, nullable=True)
    movie_release_date = Column(Date, nullable=True)
    movie_country_origin = Column(String, nullable=True)

    actors = relationship("Actor", secondary="movie_actor", back_populates="movies")
    directors = relationship("Director", secondary="director_movie", back_populates="movies_director")

class Series(Base):
    __tablename__ = "series"

    series_id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)

    series_title = Column(String, nullable=False)
    series_user_rating = Column(Float, nullable=True)
    series_critic_rating = Column(Float, nullable=True)
    avg_episode_duration = Column(Integer, nullable=True)
    series_description = Column(Text, nullable=True)
    series_release_date = Column(Date, nullable=True)
    series_country_origin = Column(String, nullable=True)


class MovieActor(Base):
    __tablename__ = "movie_actor"

    movie_id = Column(Uuid(as_uuid=True), ForeignKey("movie.movie_id"), primary_key=True)
    actor_id = Column(Uuid(as_uuid=True), ForeignKey("actor.actor_id"), primary_key=True)

class DirectorMovie(Base):
    __tablename__ = "director_movie"

    movie_id = Column(Uuid(as_uuid=True), ForeignKey("movie.movie_id"), primary_key=True)
    director_id = Column(Uuid(as_uuid=True), ForeignKey("director.director_id"), primary_key=True)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session