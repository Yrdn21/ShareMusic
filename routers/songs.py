from fastapi import APIRouter, HTTPException, status
from models.songs import SongBase, SongID
from data.db import songs_operations_db as ops


router = APIRouter(prefix="/songs", tags=["Songs"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SongID, response_description="The song has been created")
def create_song(song: SongBase):
    return ops.create_song_db(song)


@router.get("/show", status_code=status.HTTP_200_OK,response_model=list[SongID], response_description="Showing all songs")
def show_all_songs():
    song = ops.show_all_songs()
    if not song:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    return song

@router.get("/search/{song_name}", status_code=status.HTTP_200_OK, response_model=SongID, response_description = "Showing the song with the matching name")
def show_one_song_by_name(song_name: str):
    song = ops.show_song_by_name_db(song_name)
    if not song:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    return song


@router.get("/{song_id}", status_code=status.HTTP_200_OK, response_model=SongID, response_description = "Showing the songs with the matching id")
def show_one_song_by_id(song_id: int):
    song = ops.show_one_song_db(song_id)
    if not song:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    return song


@router.patch("/{song_id}/update", status_code=status.HTTP_200_OK, response_model=SongID, response_description = "The song was updated")
def update_song(song_id: int, song_data: SongBase):
    update_song = ops.update_song_db(song_id, song_data)
    if not update_song:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    return update_song


@router.delete("/{song_id}/deletesong", status_code=status.HTTP_200_OK, response_model=SongID, response_description="The song has been deleted")
def delete_song_(song_id: int):
    delete = ops.delete_song_db(song_id)
    if not delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    return delete