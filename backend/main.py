from fastapi import FastAPI
from src.app import router
app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Sigma"}