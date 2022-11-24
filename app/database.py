from fastapi.logger import logger
import os
import secrets

# configuration used to connect to MongoDB
# TODO: replace with real db
config = {
  'host': os.environ['MONGO_HOST'],
  'port': 27017,
  'user': os.environ['MONGO_USERNAME'],
  'password': os.environ['MONGO_PASSWORD'],
  'database': os.environ['MONGO_DB_NAME']
}

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
