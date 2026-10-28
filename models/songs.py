from pydantic import BaseModel


class Song(BaseModel):
    nombre: str


class SongID(Song):
    song_id: int