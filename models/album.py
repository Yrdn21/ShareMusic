from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Column, JSON

from enums.genre import Genre
from enums.ActiveStatus import ActiveStatus
from enums.editions import Edition
from models.artist import Artist
from models.songs import Song
from typing import List, Optional



class AlbumBase(SQLModel):
    title: str
    artist: Artist = Field(sa_column=Column(JSON))
    songs: List[Song] = Field(sa_column=Column(JSON))
    genre: Genre
    release_year: int
    edition: Edition = Edition.STANDARD
    status: ActiveStatus = ActiveStatus.ACTIVE


class AlbumID(AlbumBase, table=True):
    album_id: Optional[int] = Field(default=None, primary_key=True)

class AlbumStatusUpdate(SQLModel):
    status: ActiveStatus

class AlbumEditionUpdate(SQLModel):
    edition: Edition