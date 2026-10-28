from fastapi import APIRouter, HTTPException, status
from models.songs import Song, SongID

import data.songs as data_songs



router = APIRouter(prefix="/songs", tags=["Songs"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SongID, response_description="The song has been created")
def create_song(song: Song):
    return data_songs.create_song(song)


@router.get("/show", status_code=status.HTTP_200_OK,response_model=list[SongID], response_description="Showing all songs")
def show_all_songs():
    song = data_songs.read_all_songs()
    if song:
        return song
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No songs found yet")


@router.get("/{song_id}", status_code=status.HTTP_200_OK, response_model=SongID, response_description = "Showing the songs with the matching id")
def show_one_song_by_id(song_id: int):
    song = data_songs.read_song_by_id(song_id)
    if song:
        return song
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No song found")


@router.get("/search/{song_name}", status_code=status.HTTP_200_OK, response_model=SongID, response_description = "Showing the song with the matching name")
def show_one_song_by_name(song_name: str):
    song = data_songs.read_song_by_name(song_name)
    if song:
        return song
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No song found")



@router.patch("/{song_id}/update", status_code=status.HTTP_200_OK, response_model=SongID, response_description = "The song was updated")
def update_song(song_id: int, song_data: Song):
    song = data_songs.update_song(song_id, song_data)
    if song:
        return song
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The update was not successful")


@router.delete("/{song_id}/deletesong", status_code=status.HTTP_200_OK, response_model=SongID, response_description="The song has been deleted")
def delete_artist_status(song_id: int):
    delete = data_songs.delete_song(song_id)

    if not delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")

    return delete