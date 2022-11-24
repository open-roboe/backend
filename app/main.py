from fastapi import FastAPI, Depends, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.logger import logger
from .routers import account, course, websocket # import here other routes


description="""
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
app.include_router(websocket.router)
# activate here other imported routes
