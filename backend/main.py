from fastapi import FastAPI

from src.app import router as movie_router
from src.actors import router as actor_router


app = FastAPI()

app.include_router(movie_router)
app.include_router(actor_router)

@app.get("/")
async def root():
    return {"message": "Sigma"}