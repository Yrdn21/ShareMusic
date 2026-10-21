from pydantic import BaseModel
from enums.genre import Genre
from enums.ActiveStatus import ActiveStatus


class AlbumBase(BaseModel):
    title: str
    artist: str
    genre: Genre
    length: int
    release_date: str
    status: ActiveStatus


class AlbumID(AlbumBase):
    album_id: int