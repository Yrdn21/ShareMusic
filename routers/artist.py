from fastapi import APIRouter, HTTPException, status
from models.artist import Artist, ArtistID

import data.artist as data_artist



router = APIRouter(prefix="/artist", tags=["Artist"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ArtistID, response_description="The artist was created")
def create_artist(artist: Artist):
    return data_artist.create_artist(artist)


@router.get("/show", status_code=status.HTTP_200_OK,response_model=list[ArtistID], response_description="Showing all artists")
def show_all_albums():
    artist = data_artist.read_all_list()
    if artist:
        return artist
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No artists found yet")


@router.get("/{artist_id}", status_code=status.HTTP_200_OK, response_model=ArtistID, response_description = "Showing the artist with the matching id")
def show_one_artist_by_id(album_id: int):
    artist = data_artist.read_artist_by_id(album_id)
    if artist:
        return artist
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No artists found")


@router.get("/{artist_name}", status_code=status.HTTP_200_OK, response_model=ArtistID, response_description = "Showing the artist with the matching name")
def show_one_artist_by_name(album_name: str):
    artist = data_artist.read_artist_by_name(album_name)
    if artist:
        return artist
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No artists found")



@router.patch("/{artist_id}/update", status_code=status.HTTP_200_OK, response_model=ArtistID, response_description = "The artist was updated")
def update_artist(album_id: int, artist_data: Artist):
    artist = data_artist.update_artist(album_id, artist_data)
    if artist:
        return artist
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The update was not successful")


@router.delete("/{artist_id}/deleteartist", status_code=status.HTTP_204_NO_CONTENT, response_model=ArtistID, response_description = "The artist was deleted")
def delete_artist(artist_id: int):
    artist = data_artist.delete_artist(artist_id)
    if artist:
        return artist
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The delete was not successful")