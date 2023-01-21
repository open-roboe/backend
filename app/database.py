from fastapi.logger import logger
import os
from sqlmodel import Field, SQLModel, create_engine

config = {
  'sqlite_file': os.environ['SQLITE_FILE']
}

sqlite_url = f"sqlite:///testdb.db"
engine = create_engine(sqlite_url, echo=True)

# fake db
db = {
    "bob": {
        "username": "bob",
        "hashed_password": "password",
        "disabled": False,
        "admin": False
    },
    "alice": {
        "username": "alice",
        "hashed_password": "password",
        "disabled": True,
        "admin": True
    },
}

def get_db():
  """Return the MongoDb Scanner database
  """
  return db
