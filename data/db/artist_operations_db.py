from sqlmodel import Session, select
from models.artist import ArtistID, ArtistBase
from .album import engine


def create_artist_db(new_artist: ArtistBase):
    with Session(engine) as session:
        artist_db = ArtistID.model_validate(new_artist)
        session.add(artist_db)
        session.commit()
        session.refresh(artist_db)
        return artist_db


def show_all_artist_db():
    with Session(engine) as session:
        return session.exec(select(ArtistID)).all()


def show_one_artist_db(artist_id: int):
    with Session(engine) as session:
        return session.get(ArtistID, artist_id)


def show_artist_by_name_db(artist_name: str):
    with Session(engine) as session:
        statement = select(ArtistID).where(ArtistID.name.ilike(artist_name))
        return session.exec(statement).first()


def update_artist_db(artist_id: int, update_artist: ArtistBase):
    with Session(engine) as session:
        artist_db = session.get(ArtistID, artist_id)
        if not artist_db:
            return None
        artist_db.name = update_artist.name
        artist_db.country = update_artist.country
        session.add(artist_db)
        session.commit()
        session.refresh(artist_db)
        return artist_db


def delete_artist_db(artist_id: int):
    with Session(engine) as session:
        artist_db = session.get(ArtistID, artist_id)
        if not artist_db:
            return None
        session.delete(artist_db)
        session.commit()
        return artist_db