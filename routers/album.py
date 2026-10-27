from fastapi import APIRouter, status, HTTPException

from enums.ActiveStatus import ActiveStatus
from models.album import AlbumBase, AlbumID, AlbumEditionUpdate, AlbumStatusUpdate
from data import album

album_list: list[AlbumBase] = []

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_album(new_album: AlbumBase):
    result = album.create_album(new_album)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")


@router.get("/show", status_code=status.HTTP_200_OK,response_model=list[AlbumID])
def show_all_albums():
    albums = album.read_all_albums()
    if albums:
        return albums
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No albums found yet")


@router.get("/history", status_code=status.HTTP_200_OK,response_model=list[AlbumID] )
def show_deleted_albums():
    delete_ones= album.show_all_deleted_albums()
    if delete_ones:
        return delete_ones
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No delete albums yet")



@router.get(path="/search", status_code=status.HTTP_200_OK, response_model=AlbumID)
def show_one_album_by_Name(album_name: str):
    album_by_name = album.find_album_by_name(album_name)
    if not album_by_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No album found")
    else:
        return album_by_name



@router.get("/{album_id}", status_code=status.HTTP_200_OK, response_model=AlbumBase)
def show_one_album(album_id: str):
    one_album = album.read_one_album_by_id(album_id)
    if not one_album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No album found")
    else:
        return one_album



@router.patch("/{album_id}/edition", status_code=status.HTTP_200_OK, response_model=AlbumEditionUpdate)
def update_album_status(album_id: str, new_edition: AlbumEditionUpdate):
    updated = album.update_album_edition(album_id, new_edition.edition.value)

    if not updated:
        raise HTTPException(status_code = status. HTTP_404_NOT_FOUND, detail = "Album not found")

    return updated



@router.delete("/{album_id}", status_code=status.HTTP_200_OK, response_model=AlbumID)
def delete_album_status(album_id: str):
    delete = album.delete_album(album_id)

    if not delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")

    return delete
