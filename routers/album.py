from fastapi import APIRouter, status, HTTPException
from data.db.operations_db import create_album_db, show_all_animals_db, show_one_album_db,update_album_db, delete_album_db
from models.album import AlbumBase, AlbumID, AlbumStatusUpdate



router = APIRouter()


@router.get("/" , status_code=status.HTTP_201_CREATED, response_model=AlbumID)
def create_album(new_album: AlbumBase):
    return create_album_db(new_album)