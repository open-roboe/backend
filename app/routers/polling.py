from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from app.database import get_db
from sqlmodel import Field, Session, select
from app.database import engine
from ..models import database, api #"from app.models import database" is better, but not recognized by my linter lol
from app.auth import get_current_user, get_current_admin_user, get_current_super_admin_user

router = APIRouter(prefix='/api/polling', tags=['polling'])



@router.post("/roboa")
async def poll_roboa_update(roboaData: api.PollRoboaUpdate):
    """
    Polling endpoint, called repeatedly by an authenticated roboa to send its metrics
    """
    return "ok"


@router.post("/user", response_model=api.PollResponse)
async def poll_user_update(userData: api.PollUserUpdate, user = Depends()):
    """
    Polling endpoint, called repeatedly by an authenticated user to send its metrics
    and get data updates
    """
    return {
            "users": [],
            "courses": [],
            "roboas": []
            }


@router.get("/")
async def poll():
    """
    Polling endpoint, called repeatedly by an authenticated user to get data updates
    """
    with Session(engine) as session:
        users = session.exec(select(database.User)).all()
        courses = session.exec(select(database.Course)).all()
        roboas = session.exec(select(database.Roboa)).all()
        return {
                'users': users,
                'courses': courses,
                'roboas': roboas
                }


