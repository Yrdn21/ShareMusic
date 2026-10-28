from pydantic import BaseModel
from enums.genre import Genre
from enums.ActiveStatus import ActiveStatus
from enums.editions import Edition
from models.artist import Artist
from models.songs import Song
from typing import List



class AlbumBase(BaseModel):
    title: str
    artist: Artist
    songs: List[Song]
    genre: Genre
    release_year: int
    edition: Edition = Edition.STANDARD
    status: ActiveStatus = ActiveStatus.ACTIVE

class AlbumStatusUpdate(BaseModel):
    status: ActiveStatus


class AlbumID(AlbumBase):
    album_id: int


class AlbumEditionUpdate(BaseModel):
    edition: Edition