from fastapi import FastAPI

from routers import album, songs, artist

app = FastAPI()


app.include_router(album.router)
app.include_router(artist.router)
app.include_router(songs.router)