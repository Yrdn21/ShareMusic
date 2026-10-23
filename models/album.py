from pydantic import BaseModel
from enums.genre import Genre
from enums.ActiveStatus import ActiveStatus


class AlbumBase(BaseModel):
    title: str
    artist: str
    genre: Genre
    release_year: int
    status: ActiveStatus = ActiveStatus.ACTIVE
    price: float
    edition: str


class AlbumStatusUpdate(BaseModel):
    status: ActiveStatus


class AlbumID(AlbumBase):
    album_id: int
