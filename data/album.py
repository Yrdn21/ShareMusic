import csv
from models.album import AlbumBase
from enum import *


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

def write_album_into_csv(register: AlbumBase):
    with open(data_base, mode="w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)
        writer.writerow(register.model_dump())

