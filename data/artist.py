import csv
import os.path
import json


from models.artist import Artist, ArtistID


data_base = "artist.csv"
delete_data_base = "deleted_artist.csv"

column_fields = [
    "artist_id",
    "name",
    "country"
]


def artist_auto_id():
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            return max(int(row["artist_id"]) for row in reader) + 1
    except (FileNotFoundError, ValueError):
        return 1


def write_artist_into_csv(register: ArtistID):
    file_exists = os.path.isfile(data_base) and os.path.getsize(data_base) > 0
    with open(data_base, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)

        if not file_exists:
            writer.writeheader()
        writer.writerow(register.model_dump())


def create_artist(register: Artist):
    new_id = artist_auto_id()
    new_artist = ArtistID(artist_id=new_id, **register.model_dump())
    write_artist_into_csv(new_artist)
    return new_artist


def read_all_list():
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            return [ArtistID(**row) for row in reader]
    except (FileNotFoundError, ValueError):
        return []


def show_all_deleted_artists():
    try:
        with open(delete_data_base) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)

            artist = []
            for row in reader:
                artist_name = row.pop("artist_name")
                artist_country = row.pop("artist_country")

                row["artist"] = {
                    "name": artist_name,
                    "country": artist_country
                }
                row["songs"] = json.loads(row["songs"])

                artist.append(ArtistID(**row))
            return artist
    except (FileNotFoundError, ValueError):
        return None


def read_artist_by_id(artist_id: int):
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            for row in reader:
                if int(row["artist_id"]) == artist_id:
                    return ArtistID(**row)
            return None
    except (FileNotFoundError, ValueError):
        return None

def read_artist_by_name(artist_name: str):
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            for row in reader:
                if int(row["name"].lower()) == artist_name.lower():
                    return ArtistID(**row)
            return None
    except (FileNotFoundError, ValueError):
        return None


def update_artist(artist_id: int, updated_data: Artist):
    updated_artist = None
    all_artist = []
    try:
        with open(data_base, "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)
            for row in reader:
                if int(row["artist_id"]) == artist_id:
                    updated_artist = ArtistID(artist_id = artist_id, **updated_data.model_dump())
                    all_artist.append(updated_artist.model_dump())
                else:
                    all_artist.append(row)

        if updated_artist:
            with open(data_base, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=column_fields)
                writer.writeheader()
                writer.writerows(all_artist)

        return updated_artist
    except (FileNotFoundError, ValueError):
        return None


def delete_artist(artist_id: int):
    deleted_artist = None
    all_artist = []
    delete_row = None

    try:
        with open(data_base) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            next(reader, None)

            for row in reader:
                if int(row["artist_id"]) == artist_id:
                    delete_row = row.copy()


                    deleted_artist = ArtistID(**row)

                else:
                    all_artist.append(row)

        if deleted_artist and delete_row:
            with open(data_base, mode="w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=column_fields)
                writer.writeheader()
                writer.writerows(all_artist)

            file_exists = os.path.isfile(delete_data_base) and os.path.getsize(delete_data_base) > 0

            with open(delete_data_base, mode="a", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=column_fields)

                if not file_exists:
                    writer.writeheader()

                writer.writerow(delete_row)

            return deleted_artist

    except (FileNotFoundError, ValueError):
        return None