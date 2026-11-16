from sqlmodel import Session, select
from enums.ActiveStatus import ActiveStatus
from models.album import AlbumID,AlbumBase, AlbumStatusUpdate
from .album import engine


def create_album_db(new_album: AlbumBase):
    with Session(engine) as session:
        album_db = AlbumID.model_validate(new_album)
        session.add(album_db)
        session.commit()
        session.refresh(album_db)

        return album_db


def show_all_albums_db():
    with Session(engine) as session:
        statement = select(AlbumID).where(AlbumID.status == ActiveStatus.ACTIVE)
        return session.exec(statement).all()


def show_all_deleted_albums_db():
    with Session(engine) as session:
        statement = select(AlbumID).where(AlbumID.status == ActiveStatus.INACTIVE)
        return session.exec(statement).all()


def show_one_album_db(album_id: int):
    with Session(engine) as session:
        return (session.get(AlbumID, album_id))


def show_one_album_by_name_db(album_name: str):
    with Session(engine) as session:
        statement = select(AlbumID).where(AlbumID.title.ilike(album_name))
        return session.exec(statement).first()


def update_album_db(album_id: int, status_update:AlbumStatusUpdate):
    with Session(engine) as session:
        album_db = session.get(AlbumID, album_id)
        if not album_db:
            return None
        album_db.status = status_update.status
        session.add(album_db)
        session.commit()
        session.refresh(album_db)
        return album_db

def delete_album_db(album_id: int):
    inactive_status = AlbumStatusUpdate (status = ActiveStatus.INACTIVE)
    return update_album_db(album_id, inactive_status)