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


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=AlbumID)
def show_one_album_by_id(id: str):
    one_album = show_one_album_db(id)
    if not one_album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
    else:
        return one_album


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=AlbumID)
def update_album_by_id(id: str, new_status: AlbumStatusUpdate):
    return update_album_db(id, new_status)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_album_by_id(id: str):
    delete_album_db(id)
    return show_one_album_db(id)
