from typing import Optional
from sqlmodel import SQLModel, Field

class ArtistBase(SQLModel):
    name: str
    country: str = "Desconocido"

class ArtistID(ArtistBase, table=True):
    artist_id: Optional[int] = Field(default=None, primary_key=True)