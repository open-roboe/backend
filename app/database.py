from fastapi.logger import logger
import os
from sqlmodel import Field, SQLModel, Session, create_engine

config = {
  'sqlite_file': os.environ['SQLITE_FILE']
}

sqlite_url = f"sqlite:///" #in-memory database
engine = create_engine(sqlite_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

