from typing import Optional
from sqlmodel import SQLModel, Field

class SongBase(SQLModel):
    nombre: str

class SongID(SongBase, table=True):
    song_id: Optional[int] = Field(default=None, primary_key=True)