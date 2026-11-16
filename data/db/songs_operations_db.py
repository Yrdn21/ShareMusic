from sqlmodel import Session, select
from models.songs import SongID, SongBase
from .album import engine


def create_song_db(new_song: SongBase):
    with Session(engine) as session:
        song_db = SongID.model_validate(new_song)
        session.add(song_db)
        session.commit()
        session.refresh(song_db)
        return song_db


def show_all_songs():
    with Session(engine) as session:
        return session.exec(select(SongID)).all()


def show_one_song_db(song_id: int):
    with Session(engine) as session:
        return session.get(SongID, song_id)


def show_song_by_name_db(name: str):
    with Session(engine) as session:
        statement = select(SongID).where(SongID.nombre.ilike(name))
        return session.exec(statement).first()


def update_song_db(song_id: int, updated_song: SongBase):
    with Session(engine) as session:
        song_db = session.get(SongID, song_id)
        if not song_db:
            return None
        song_db.nombre = updated_song.nombre
        session.add(song_db)
        session.commit()
        session.refresh(song_db)
        return song_db


def delete_song_db(song_id: int):
    with Session(engine) as session:
        song_db = session.get(SongID, song_id)
        if not song_db:
            return None
        session.delete(song_db)
        session.commit()
        return song_db