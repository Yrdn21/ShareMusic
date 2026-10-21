from pydantic import BaseModel


class AlbumBase(BaseModel):
    album_id: int #TODO auto_id
    title: str
    artist: str
    genre: str
    length: int
    release_date: str
    status: str #TODO status active and inactive




