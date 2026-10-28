from fastapi import FastAPI

from models import artist
from routers import album, song, artist

app = FastAPI()


app.include_router(album.router)
app.include_router(artist.router)
app.include_router(song.router)