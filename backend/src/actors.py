from fastapi import APIRouter, HTTPException
from src.schemas.actor import ActorCreate
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from uuid import UUID
from src.db import Actor, get_async_session
from sqlalchemy import select

router = APIRouter()

actors_list = {}


@router.get("/actors_list")
def get_actor():
    return actors_list

@router.get("/actor/{id}")
def get_actor_id(id: int):

    if id not in actors_list:
        raise HTTPException(
            status_code=404,
            detail="actor was not found"
        )

    return actors_list[id]



@router.post("/actors_list")
async def add_actor(actor: ActorCreate,
              session: AsyncSession = Depends(get_async_session)):

    new_actor = Actor(
        name = actor.name,
        surname = actor.surname,
        birth_date = actor.birthdate
    )

    session.add(new_actor)

    await session.commit()

    await session.refresh(new_actor)

    return new_actor
