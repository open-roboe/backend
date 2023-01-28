from fastapi.logger import logger
import os
from sqlmodel import Field, SQLModel, Session, create_engine

config = {
    'sqlite_file': os.environ['SQLITE_FILE']
}

filename = config["sqlite_file"]
# sqlite_url = f"sqlite:///"  # in-memory database
sqlite_url = f"sqlite:///{filename}"
engine = create_engine(sqlite_url,
                       echo=True,
                       # This suppress an error, thrown every time an endpoint uses get_session as a dependency
                       # TODO: check if the error we are suppressing is actually a problem
                       # https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#threading-pooling-behavior
                       connect_args={'check_same_thread': False},
                       )


def get_session():
    with Session(engine) as session:
        yield session
