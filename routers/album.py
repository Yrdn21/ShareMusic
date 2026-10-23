from fastapi import APIRouter, status, HTTPException
from data.db.operations_db import create_album_db, show_all_albums_db, show_one_album_db,update_album_db, delete_album_db
from models.album import AlbumBase, AlbumID, AlbumStatusUpdate



router = APIRouter()


@router.post("/" , status_code=status.HTTP_201_CREATED, response_model=AlbumID)
def create_album(new_album: AlbumBase):
    return create_album_db(new_album)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[AlbumID])
def show_all_albums():
    return show_all_albums_db()