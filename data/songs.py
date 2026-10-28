import csv
import os.path
from models.songs import Song, SongID

data_base = "songs.csv"
column_fields = [
    "song_id",
    "nombre"
]

def song_auto_id():
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            return max(int(row["song_id"]) for row in reader) + 1
    except (FileNotFoundError, ValueError):
        return 1


def create_song(register: Song) -> SongID:
    new_id = song_auto_id()
    new_song = SongID(song_id=new_id, **register.model_dump())

    file_exists = os.path.isfile(data_base) and os.path.getsize(data_base) > 0
    with open(data_base, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)
        if not file_exists:
            writer.writeheader()
        writer.writerow(new_song.model_dump())
    return new_song


def read_all_songs(song_id: int):
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            for row in reader:
                if int(row["song_id"]) == song_id:
                    return SongID(**row)
            return None
    except (FileNotFoundError, ValueError):
        return None


def read_song_by_id(song_id: int):
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            for row in reader:
                if int(row["song_id"]) == song_id:
                    return SongID(**row)
            return None
    except (FileNotFoundError, ValueError):
        return None


def read_song_by_name(song_name: str):
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            for row in reader:
                if int(row["nombre"].lower()) == song_name.lower():
                    return SongID(**row)
            return None
    except (FileNotFoundError, ValueError):
        return None


def update_song(song_id: int, updated_data: Song):
    update_song = None
    all_songs = []
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            for row in reader:
                if int(row["song_id"]) == song_id:
                    update_song = SongID(song_id=song_id, **updated_data.model_dump())
                    all_songs.append(row)

        if update_song:
            with open(data_base, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=column_fields)
                writer.writeheader()
                writer.writerow(all_songs)

        return update_song
    except FileNotFoundError:
        return None


def delete_song(song_id: int):
    deleted_song = None
    all_songs = []
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            for row in reader:
                if int(row["song_id"]) == song_id:
                    deleted_song = SongID(**row)
                else:
                    all_songs.append(row)

            if deleted_song:
                with open(data_base, "w", newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=column_fields)
                    writer.writeheader()
                    writer.writerow(all_songs)

            return deleted_song
    except (FileNotFoundError, ValueError):
        return None