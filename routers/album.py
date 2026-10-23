from fastapi import APIRouter, status, HTTPException
from models.album import AlbumBase, AlbumID
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


@router.get("/", status_code=status.HTTP_200_OK,response_model=list[AlbumID])
def show_all_albums():
    albums = album.read_all_albums()
    return albums



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


