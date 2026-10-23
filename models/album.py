from typing import Optional
from sqlmodel import Field, SQLModel

from enums.genre import Genre
from enums.ActiveStatus import ActiveStatus


class AlbumBase(SQLModel):
    title: str
    artist: str
    genre: Genre
    release_year: int
    status: ActiveStatus = ActiveStatus.ACTIVE


class AlbumStatusUpdate(SQLModel):
    status: ActiveStatus


class AlbumID(AlbumBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)