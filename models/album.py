from pydantic import BaseModel
from enums.genre import Genre
from enums.ActiveStatus import ActiveStatus
from enums.editions import Edition


class AlbumBase(BaseModel):
    title: str
    artist: str
    genre: Genre
    release_year: int
    status: ActiveStatus = ActiveStatus.ACTIVE
    edition: Edition = Edition.STANDARD


class AlbumStatusUpdate(BaseModel):
    status: ActiveStatus


class AlbumID(AlbumBase):
    album_id: int


class AlbumEditionUpdate(BaseModel):
    edition: Edition