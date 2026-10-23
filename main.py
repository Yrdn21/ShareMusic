from fastapi import FastAPI
from data.db.album import create_db_tables
from routers import album

app = FastAPI()



@app.on_event("startup")
def on_startup():
    create_db_tables()


app.include_router(router=album.router, prefix="/album", tags=["album"])