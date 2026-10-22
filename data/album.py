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


