from fastapi import APIRouter, HTTPException

router = APIRouter()

actors_list = {}


@router.get("actors")
def get_actor():
    return actors_list