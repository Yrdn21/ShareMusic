from pydantic import BaseModel



class Song(BaseModel):
    track_id: int
    title: str