from fastapi import APIRouter, HTTPException, status
from models.artist import ArtistID, ArtistBase
from data.db import artist_operations_db as ops



router = APIRouter(prefix="/artist", tags=["Artist"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ArtistID, response_description="The artist was created")
def create_artist(artist: ArtistBase):
    return ops.create_artist_db(artist)


@router.get("/show", status_code=status.HTTP_200_OK, response_model=list[ArtistID], response_description="Showing all artists")
def show_all_artist():
    return ops.show_all_artist_db()


@router.get("/search", status_code=status.HTTP_200_OK, response_model=ArtistID, response_description="Showing the artist with the matching name")
def show_one_artist_by_name(artist_name: str):
    artist = ops.show_artist_by_name_db(artist_name)
    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No artists found")
    return artist


@router.get("/{artist_id}", status_code=status.HTTP_200_OK, response_model=ArtistID, response_description = "Showing the artist with the matching id")
def show_one_artist_by_id(artist_id: int):
    artist = ops.show_one_artist_db(artist_id)
    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No artists found")
    return artist


@router.patch("/{artist_id}/update", status_code=status.HTTP_200_OK, response_model=ArtistID, response_description = "The artist was updated")
def update_artist(artist_id: int, artist_data: ArtistBase):
    update = ops.update_artist_db(artist_id, artist_data)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No artists found")
    return update



@router.delete("/{artist_id}/deleteartist", status_code=status.HTTP_200_OK, response_model=ArtistID, response_description="The artist has been deleted")
def delete_artist(artist_id: int):
    delete = ops.delete_artist_db(artist_id)
    if not delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No artists found")
    return delete