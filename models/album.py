from pydantic import BaseModel
from enums.genre import Genre
from enums.ActiveStatus import ActiveStatus


class AlbumBase(BaseModel):
    album_id: int #TODO auto_id
    title: str
    artist: str
    genre: Genre
    length: int
    release_date: str
    status: ActiveStatus




