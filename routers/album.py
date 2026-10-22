from fastapi import APIRouter, status, HTTPException
from models.album import AlbumBase
from data import album


album_list:list[AlbumBase] =[]


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_album(new_album: AlbumBase):
    result = album.create_album(new_album)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "Album not found")

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[AlbumBase])
def show_all_albums():
    albums_list = album.read_all_albums()
    if not albums_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No albums found"
        )
    return albums_list

@router.get("/{album_id}", status_code=status.HTTP_200_OK, response_model=AlbumBase)
def show_one_album(album_id: str):
    one_album = album.read_one_album_by_id(album_id)
    if not one_album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No album found")
    else:
        return one_album
