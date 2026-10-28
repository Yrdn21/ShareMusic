from pydantic import BaseModel



class Artist(BaseModel):
    name: str
    country: str="Desconocido"

class ArtistID(Artist):
    artist_id: int