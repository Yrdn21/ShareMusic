from fastapi import FastAPI
from routers import album


app = FastAPI()


app.include_router(album.router, prefix="/album", tags=["album"])
