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

db = { }

def get_db():
  """Return the MongoDb Scanner database
  """
  return db
