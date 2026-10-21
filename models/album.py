from pydantic import BaseModel


class AlbumBase(BaseModel):
    album_id: int
    title: str
    artist: str
    genre: str
    length: int
    release_date: str


