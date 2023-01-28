from fastapi import FastAPI, Depends, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.logger import logger

from sqlmodel import SQLModel
from .models import database  # importing the database models allow SQLModel to automatically generate the database
from .database import engine

from .routers import account, course, polling, roboa  # import here other routes

description = """
### backend server for the roboapp, connecting roboe with the android clients
"""

app = FastAPI(
    title="roboe backend",
    description=description,
    version="0.0.1",
    contact={
        "name": "",
        "url": "https://github.com/open-roboe"
    },
)


# TODO: replace with real migration system
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


# During development, the webserver runs on a separate origin
# therefore a CORS configuration on the api server is required.
# In production the api server will be behind the same
# reverse-proxy serving the static website, so there won't be any CORS issue
origins = [
    "http://roboa.local",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account.router)
app.include_router(course.router)
app.include_router(polling.router)
app.include_router(roboa.router)
# activate here other imported routes
