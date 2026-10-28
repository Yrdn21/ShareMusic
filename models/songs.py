from pydantic import BaseModel


class Song(BaseModel):
    nombre: str