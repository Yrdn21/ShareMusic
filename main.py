from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import album,artist,songs
from data.db.album import create_db_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_tables()
    yield

app = FastAPI()

app.include_router(album.router)
app.include_router(artist.router)
app.include_router(songs.router)