import csv
from models.album import AlbumBase, AlbumID
from enums.genre import Genre
from enums.ActiveStatus import ActiveStatus

data_base = "album.csv"

column_fields =[
    "album_id"
    "title"
    "artist"
    "genre"
    "length"
    "release_date"
    "status"
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
    with open(data_base, mode="a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields,)
        writer.writerow(register.model_dump())


def create_album(register: AlbumBase):
    new_id =  auto_id()
    new_album_ID = AlbumID(album_id = new_id, **album.model_dump())
    write_album_into_csv(new_album_ID)
    return new_album_ID


