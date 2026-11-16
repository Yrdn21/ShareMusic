from fastapi import APIRouter, status, HTTPException
from models.album import AlbumBase, AlbumID, AlbumStatusUpdate, AlbumEditionUpdate
from data.db import operations_db



router = APIRouter(prefix="/albums", tags=["Albums"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AlbumID, response_description = "Album created successfully")
def create_album(new_album: AlbumBase):
    return operations_db.create_album_db(new_album)


@router.get("/show", status_code=status.HTTP_200_OK,response_model=list[AlbumID], response_description="Showing all albums")
def show_all_albums():
    return operations_db.show_all_albums_db()


@router.get("/history", status_code=status.HTTP_200_OK,response_model=list[AlbumID], response_description="Showing deleted albums")
def show_deleted_albums():
    return operations_db.show_all_deleted_albums_db()



@router.get(path="/search", status_code=status.HTTP_200_OK, response_model=AlbumID, response_description="Showing the album with the matching name")
def show_one_album_by_Name(album_name: str):
    album = operations_db.show_one_album_by_name_db(album_name)
    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No album found")
    return album



@router.get("/{album_id}", status_code=status.HTTP_200_OK, response_model=AlbumID, response_description="Showing the album with the matching id")
def show_one_album(album_id: int):
    album = operations_db.show_one_album_db(album_id)
    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No album found")
    return album



@router.patch("/{album_id}/edition", status_code=status.HTTP_200_OK, response_model=AlbumID, response_description="The edition of the album has been updated")
def update_album_status(album_id: int, new_edition: AlbumEditionUpdate):
    update = operations_db.update_album_edition_db(album_id, new_edition)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
    return update



@router.delete("/{album_id}/deletealbum", status_code=status.HTTP_200_OK, response_model=AlbumID, response_description="The album has been deleted")
def delete_album_status(album_id: int):
    delete = operations_db.delete_album_db(album_id)
    if not delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
    return delete
