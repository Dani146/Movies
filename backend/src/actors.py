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
async def get_actor(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Actor))
    actors = result.scalars().all()
    return actors
    

@router.get("/actor/{id}")
async def get_actor_id(id: UUID,
                 session: AsyncSession = Depends(get_async_session)):

    actor = await session.get(Actor, id)

    if actor is None:
        raise HTTPException(
            status_code=404,
            detail="Actor was not found"
        ) 

    return actor

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

    print("works")
    return new_actor


@router.delete("/actor/{id}")
async def delete_actor(id: UUID,
                       session: AsyncSession = Depends(get_async_session)):
    actor = await session.get(Actor, id)

    if actor is None:
        raise HTTPException(
            status_code=404,
            detail="actor does not exist"
        )
    
    await session.delete(actor)
    await session.commit()
    return {"message": "actor was deleted sucessfully"}
