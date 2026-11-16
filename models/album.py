from typing import List, Optional, Dict, Any
from sqlmodel import SQLModel, Field, Column, JSON
from enums.genre import Genre
from enums.ActiveStatus import ActiveStatus
from enums.editions import Edition
from models.artist import ArtistBase as Artist
from models.songs import SongBase as Song


class AlbumBase(SQLModel):
    title: str
    artist: Artist
    songs: List[Song]
    genre: Genre
    release_year: int
    edition: Edition = Edition.STANDARD
    status: ActiveStatus = ActiveStatus.ACTIVE


class AlbumID(SQLModel, table=True):
    album_id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    artist: Dict[str, Any] = Field(sa_column=Column(JSON))
    songs: List[Dict[str, Any]] = Field(sa_column=Column(JSON))
    genre: Genre
    release_year: int
    edition: Edition = Edition.STANDARD
    status: ActiveStatus = ActiveStatus.ACTIVE


class AlbumStatusUpdate(SQLModel):
    status: ActiveStatus


class AlbumEditionUpdate(SQLModel):
    edition: Edition