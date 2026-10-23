from enums import ActiveStatus
from models.album import AlbumID, AlbumBase, AlbumStatusUpdate
from sqlmodel import SQLModel, Session, select
from .album import engine


def create_album_db(new_album: AlbumBase):
    session = Session(engine)
    album_db = AlbumID(**new_album.model_dump())
    session.add(album_db)
    session.commit()
    session.refresh(album_db)
    session.close()

    return album_db

def show_all_albums_db():
    session= Session(engine)

    animals = session.exec(select(AlbumID)).all()
    session.close()
    return animals

def show_one_album_db(album_id: int):
    session= Session(engine)
    album_db = session.get(AlbumID, album_id)
    session.close()
    return album_db


def update_album_db(album_id: int, status:AlbumStatusUpdate):
    session= Session(engine)
    album_db = session.get(AlbumID, album_id)
    print(status)
    album_db.status = status.status
    session.add(album_db)
    session.commit()
    session.refresh(album_db)

    session.close()
    return album_db

def delete_album_db(album_id: int):
    session= Session(engine)
    update_album_db(album_id, status=ActiveStatus.INACTIVE)
    session.commit()
    session.close()

    return True