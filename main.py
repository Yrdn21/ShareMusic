from fastapi import FastAPI
from routers import album


app = FastAPI()


app.include_router(album.router, prefix="/album", tags=["album"])
app.include_router(album.router, prefix="/artist", tags=["artist"])
app.include_router(album.router, prefix="/songs", tags=["songs"])