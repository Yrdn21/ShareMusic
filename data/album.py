import csv
import os.path
import json

from starlette.exceptions import HTTPException

from enums.ActiveStatus import ActiveStatus
from models.album import AlbumBase, AlbumID


data_base = "album.csv"
delete_data_base = "delete_albums.csv"

column_fields = [
    "album_id",
    "title",
    "artist",
    "songs",
    "genre",
    "release_year",
    "edition",
    "status",
]


def album_auto_id():
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            max_id = max(int(row["album_id"]) for row in reader)
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1



def write_album_into_csv(register: AlbumID):
    file_exists = os.path.isfile(data_base) and os.path.getsize(data_base) > 0

    data = register.model_dump()

    data["artist"] = json.dumps(data["artist"])
    data["songs"] = json.dumps(data["songs"])

    with open(data_base, mode="a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)


        if not file_exists:
            writer.writeheader()

        writer.writerow(data)



def create_album(register: AlbumBase):
    new_id = album_auto_id()
    new_album_ID = AlbumID(album_id=new_id, **register.model_dump())
    write_album_into_csv(new_album_ID)
    return new_album_ID




def read_all_albums():
    try:
        with open(data_base) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)

            albums = []
            for row in reader:
                row["artist"] = json.loads(row["artist"])
                row["songs"] = json.loads(row["songs"])
                albums.append(AlbumID(**row))

            return albums
    except (FileNotFoundError, ValueError):
        return []


def show_all_deleted_albums():
    try:
        with open(delete_data_base) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)

            albums = []
            for row in reader:
                row["artist"] = json.loads(row["artist"])
                row["songs"] = json.loads(row["songs"])
                albums.append(AlbumID(**row))

            return albums
    except (FileNotFoundError, ValueError):
        return []


def read_one_album_by_id(album_id: str):
    try:
        with open(data_base) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)

            for row in reader:
                if row["album_id"] == album_id:
                    row["artist"] = json.loads(row["artist"])
                    row["songs"] = json.loads(row["songs"])
                    return AlbumBase(**row)
            return None

    except FileNotFoundError:
        return None



def find_album_by_name(album_name: str):
    try:
        with open(data_base) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)

            for row in reader:
                if row["title"].lower() == album_name.lower():
                    return AlbumID(**row)
    except FileNotFoundError:
        return None
    return None


def update_album_edition(album_id: str, new_edition: str):
    updated_album=None
    all_albums=[]

    try:
        with open(data_base) as csvfile:
            reader =csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)

            for row in reader:
                if row["album_id"] == album_id:
                    row["edition"] = new_edition
                    updated_album =  AlbumID(**row)

                all_albums.append(row)

        if updated_album:
            with open(data_base, mode="w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=column_fields)
                writer.writeheader()
                writer.writerows(all_albums)

        return updated_album

    except FileNotFoundError:
        return updated_album


def delete_album(album_id: str):
    deleted_album=None
    all_albums=[]

    try:
        with open(data_base) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)

            for row in reader:
                if row["album_id"] == album_id:
                    row["status"] = ActiveStatus.INACTIVE.value
                    deleted_album = AlbumID(**row)

                else:
                    all_albums.append(row)

        if deleted_album:
            with open(data_base, mode = "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=column_fields)
                writer.writeheader()
                writer.writerows(all_albums)


            file_exists = os.path.isfile(delete_data_base) and os.path.getsize(delete_data_base) > 0

            with open(delete_data_base, mode="a", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=column_fields)

                if not file_exists:
                    writer.writeheader()

                writer.writerow(deleted_album.model_dump())

            return deleted_album

    except FileNotFoundError:
        return None