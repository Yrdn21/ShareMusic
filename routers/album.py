from fastapi import APIRouter, status, HTTPException
from models.album import AlbumBase, AlbumID, AlbumStatusUpdate
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


@router.get("/{album_id}", status_code=status.HTTP_200_OK, response_model=AlbumBase)
def show_one_album(album_id: str):
    one_album = album.read_one_album_by_id(album_id)
    if not one_album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No album found")
    else:
        return one_album


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[AlbumID])
def show_all_albums():
    return album.read_all_albums()




@router.patch("/{album_id}", status_code=status.HTTP_200_OK)
def update_album_status(album_id: str, status_update: AlbumStatusUpdate):
    updated = album.update_album_status(album_id, status_update.status)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Album not found"
        )
    return {"message": "Album actualizado :D"}


@router.delete("/{album_id}", status_code=status.HTTP_200_OK)
def delete_album(album_id: str):
    archived = album.delete_album(album_id)
    if not archived:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Album not found in active list"
        )
    return {
        "message": f"Album con la ID {album_id} eliminado"
    }