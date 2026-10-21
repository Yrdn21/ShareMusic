from fastapi import APIRouter, status, HTTPException
from models.album import AlbumBase
from data import album



album_list:list[AlbumBase] =[]


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_album(new_album: AlbumBase):
    status = album.create_album(new_album)
    if status:
        return status
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "Animal not found")