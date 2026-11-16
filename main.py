from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import album, artist, songs
from data.db.album import create_db_tables
# Importamos los modelos para que SQLModel los registre antes de crear las tablas
from models.album import AlbumID
from models.artist import ArtistID
from models.songs import SongID

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(album.router)
app.include_router(artist.router)
app.include_router(songs.router)