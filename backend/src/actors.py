from fastapi import APIRouter, HTTPException

router = APIRouter()

actors_list = {}


@router.get("actors_list")
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