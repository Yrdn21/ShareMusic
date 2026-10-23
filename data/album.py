import csv
from models.album import AlbumBase, AlbumID
from enums.genre import Genre
from enums.ActiveStatus import ActiveStatus

data_base = "album.csv"
data_base_inactives = "album_inactives.csv"

column_fields =[
    "album_id",
    "title",
    "artist",
    "genre",
    "release_year",
    "status",
]


def album_auto_id():
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, column_fields)
            max_id = max (int(row["album_id"]) for row in reader)
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1


def write_album_into_csv(register: AlbumID):
    file_exits = os.path.exists(data_base) and os.path.getsize(data_base) > 0
    with open(data_base, mode="a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields,)
        if not file_exits:
            writer.writeheader()
        writer.writerow(register.model_dump())


def create_album(register: AlbumBase):
    new_id = album_auto_id()
    new_album_ID = AlbumID(album_id=new_id, **register.model_dump())
    write_album_into_csv(new_album_ID)
    return new_album_ID

def read_one_album_by_id(album_id: str):
    with open(data_base) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames = column_fields)
        for row in reader:
            if row["album_id"] == album_id:
                return AlbumBase(**row)
        return None

def read_all_albums():
    albums = []
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            for row in reader:
                albums.append(AlbumID(**row))
    except (FileNotFoundError, ValueError):
        return []
    return albums


def update_album_status(album_id: str, new_status: str):
    albums = []
    updated = False

    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            for row in reader:
                if row["album_id"] == album_id:
                    row["status"] = new_status
                    updated = True
                albums.append(row)
    except FileNotFoundError:
        return False

    if updated:
        with open(data_base, mode="w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=column_fields)
            writer.writerows(albums)
    return updated


import os


def delete_album(album_id: str):
    active_albums = []
    album_to_archive = None

    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            for row in reader:
                if str(row["album_id"]) == str(album_id):
                    row["status"] = ActiveStatus.INACTIVE.value
                    album_to_archive = row
                else:
                    active_albums.append(row)
    except FileNotFoundError:
        return False

    if not album_to_archive:
        return False

    file_exists = os.path.exists(data_base_inactives) and os.path.getsize(data_base_inactives) > 0

    with open(data_base_inactives, mode="a", newline="") as history_file:
        writer = csv.DictWriter(history_file, fieldnames=column_fields)

        if not file_exists:
            writer.writeheader()

        writer.writerow(album_to_archive)

    with open(data_base, mode="w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)
        # writer.writeheader()
        writer.writerows(active_albums)

    return True